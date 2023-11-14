

import requests
from pptx import Presentation as XPresentation
from spire.presentation import *
from spire.presentation.common import *
import pandas as pd

from config import Template
from utils.mail import sendEmail

if not os.path.exists("./files"):
    os.mkdir("./files")
ppt = "./files/ppt"
if not os.path.exists(ppt):
    os.mkdir(ppt)
pdf = "./files/pdf"
if not os.path.exists(pdf):
    os.mkdir(pdf)


def genCertificate(template: int, value):
    presentation = XPresentation(f'./templates/{Template[template]}.pptx')
    for slide in presentation.slides:
        for shape in slide.shapes:
            if shape.has_text_frame:
                for paragraph in shape.text_frame.paragraphs:
                    for run in paragraph.runs:
                        if "{name}" in run.text:
                            run.text = run.text.replace("{name}", value['name'])
    presentation.save(f'{ppt}/{value["id"]}.pptx')
    result = ppt2pdf(value)
    try:
        os.remove(f'{ppt}/{value["id"]}.pptx')
    except Exception:
        pass
    try:
        os.remove(f'{pdf}/{value["id"]}.pdf')
    except Exception:
        pass
    return result

def ppt2pdf(value):
    presentation = Presentation()
    presentation.LoadFromFile(f"{ppt}/{value['id']}.pptx")
    slide = presentation.Slides[0]
    slide.SaveToFile(f"{pdf}/{value['id']}.pdf", FileFormat.PDF)
    presentation.Dispose()
    rs = requests.post("https://cerify.heimanbotz.workers.dev/certificate",
        data=value,
        files={'file': open(f"{pdf}/{value['id']}.pdf", 'rb')}
    ).json()
    if rs["success"]:
        return { "success": True, "dl": f"https://cerify.heimanbotz.workers.dev/download/{rs['id']}" }
    else:
        return { "success": False, "message": rs["message"] }



def genMassCertificate(template: int, file_path: str):
    df = pd.read_excel(file_path)
    for i in df['SL No'].unique().tolist():
        try:
            result = genCertificate(1, { 'name': df['Name'][i-1] })
            if result["success"] and sendEmail(df['Name'][i-1], df['Email'][i-1], result)["success"]:
                df['Link'][i-1] = result["dl"]
                df['Sent'][i-1] = True
                print(f"Successfully sent to {df['Name'][i-1]} ")
            else:
                df['Sent'][i-1] = False
                print(f"Failed Name: {df['Name'][i-1]} with {result['message']}")
        except Exception as e:
            df['Sent'][i-1] = False
            print(f"Failed Name: {df['Name'][i-1]} with {e}")
    df.to_excel(file_path, index=False)
    df = pd.read_excel(file_path)
    unable = []
    able = []
    for i in df['SL No'].unique().tolist():
        if not bool(df['Sent'][i-1]):
            unable.append({"name": df['Name'][i-1], "email": df['Email'][i-1]})
        else:
            able.append({"name": df['Name'][i-1], "email": df['Email'][i-1]})
    return { "success": True, "able": able, "unable": unable }
