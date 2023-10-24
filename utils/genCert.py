

import requests
from pptx import Presentation as XPresentation
from spire.presentation import *
from spire.presentation.common import *

from config import Template

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
