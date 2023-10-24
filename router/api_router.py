# (c) 2022-2023, Akkil M G (https://github.com/HeimanPictures)
# License: GNU General Public License v3.0


import requests
from fastapi import APIRouter, Request, UploadFile, File
from fastapi.responses import JSONResponse

from utils.genCert import genCertificate
router = APIRouter()

@router.post("/generate")
async def generateCertificate(request: Request, template: int, name: str, id: str):
    try:
        value = {"name": name, "id": id}
        result = genCertificate(template, value)
        if result['success']:
            return JSONResponse({ "success": True, 'dl': result['dl']})
        else:
            return JSONResponse({ "success": False, "message": result["message"]})
    except Exception as e:
        return JSONResponse({ "success": False, "message": f"Error: {e}"})


@router.post("/mass-generate")
async def generateMassNumberOfCertificate(request: Request, template: int, name: str, id: str): # file: UploadFile = File(...)):
    try:
        value = {"name": name, "id": id}
        result = genCertificate(template, value)
        if result['success']:
            return JSONResponse({ "success": True, 'dl': result['dl']})
        else:
            return JSONResponse({ "success": False, "message": result["message"]})
    except Exception as e:
        return JSONResponse({ "success": False, "message": f"Error: {e}"})