# (c) 2022-2023, Akkil M G (https://github.com/HeimanPictures)
# License: GNU General Public License v3.0


import requests
from fastapi import APIRouter, Request, UploadFile, File
from fastapi.responses import JSONResponse

from utils.genCert import genCertificate, genCertificateFromUrl
router = APIRouter()


@router.post("/template")
async def uploadTemplate(request: Request, file: UploadFile = File(...)):
    """
    Upload a template file (.pptx) to generate certificates.
    params:
        file: UploadFile
    return:
        success: bool
        message: str
        dl: str
    """
    try:
        file_content = await file.read()
        rs = requests.post("https://certify.izaries.workers.dev/certificate",
            files={'file': ('certificate.pptx', file_content, 'application/vnd.openxmlformats-officedocument.presentationml.presentation')}
        ).json()
        if rs["success"]:
            return JSONResponse({ "success": True, "dl": f"https://certify.izaries.workers.dev/download?id={rs['id']}&ext=pptx" })
        else:
            return JSONResponse({ "success": False, "message": rs["message"] })
    except Exception as e:
        return JSONResponse({ "success": False, "message": f"Error: {e}" })
    

@router.post("/generate")
async def generateCertificate(request: Request, template: int, name: str, id: str):
    """
    Generate a certificate using the uploaded template.
    params:
        template: int
        name: str
        id: str
    return:
        success: bool
        message: str
        dl: str
    """
    try:
        value = { "name": name, "id": id }
        result = genCertificate(template, value)
        if result['success']:
            return JSONResponse({ "success": True, 'dl': result['dl']})
        else:
            return JSONResponse({ "success": False, "message": result["message"]})
    except Exception as e:
        return JSONResponse({ "success": False, "message": f"Error: {e}"})
    

@router.post("/generate-email")
async def generateEmailNCertificate(request: Request, template: int, name: str, id: str, subject: str, body: str, email: str):
    """
    Generate a certificate using the uploaded template and send it to the email.
    params:
        template: int
        name: str
        id: str
        subject: str
        body: str
        email: str
    return:
        success: bool
        message: str
        dl: str
    """
    try:
        value = { "name": name, "id": id, "body": body, "subject": subject }
        result = genCertificate(template, value, email=email)
        if result['success']:
            return JSONResponse({ "success": True, 'dl': result['dl']})
        else:
            return JSONResponse({ "success": False, "message": result["message"]})
    except Exception as e:
        return JSONResponse({ "success": False, "message": f"Error: {e}"})

"""

"""



@router.post("/generate-url")
async def generateCertificate(request: Request, url: str, name: str, id: str):
        """
        Generate a certificate using the uploaded template.
        params:
            template: int
            name: str
            id: str
        return:
            success: bool
            message: str
            dl: str
        """
    # try:
        value = { "name": name, "id": id }
        result = genCertificateFromUrl(url, value)
        if result['success']:
            return JSONResponse({ "success": True, 'dl': result['dl']})
        else:
            return JSONResponse({ "success": False, "message": result["message"]})
    # except Exception as e:
    #     return JSONResponse({ "success": False, "message": f"Error: {e}"})
    

@router.post("/generate-url-email")
async def generateEmailNCertificate(request: Request, url: str, name: str, id: str, subject: str, body: str, email: str):
    """
    Generate a certificate using the uploaded template and send it to the email.
    params:
        template: int
        name: str
        id: str
        subject: str
        body: str
        email: str
    return:
        success: bool
        message: str
        dl: str
    """
    try:
        value = { "name": name, "id": id, "body": body, "subject": subject }
        result = genCertificateFromUrl(url, value, email=email)
        if result['success']:
            return JSONResponse({ "success": True, 'dl': result['dl']})
        else:
            return JSONResponse({ "success": False, "message": result["message"]})
    except Exception as e:
        return JSONResponse({ "success": False, "message": f"Error: {e}"})

