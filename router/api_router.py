# (c) 2022-2023, Akkil M G (https://github.com/HeimanPictures)
# License: GNU General Public License v3.0


import requests, os
from fastapi import APIRouter, Request, UploadFile, File
from fastapi.responses import JSONResponse

from utils.genCert import genCertificate, genMassCertificate
router = APIRouter()

@router.post("/generate")
async def generateCertificate(request: Request, template: int, name: str):
    try:
        result = genCertificate(template, { "name": name })
        if result['success']:
            return JSONResponse({ "success": True, 'dl': result['dl']})
        else:
            return JSONResponse({ "success": False, "message": result["message"]})
    except Exception as e:
        return JSONResponse({ "success": False, "message": f"Error: {e}"})


@router.post("/mass-generate")
async def generateMassNumberOfCertificate(request: Request, template: int, file: UploadFile = File(...)):
    try:
        file_path = os.path.join("./files/excel", file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
            result = genMassCertificate(template, file_path)
            if result['success']:
                return JSONResponse({ "success": True, 'able':result["able"] , 'unable': result["unable"] })
            else:
                return JSONResponse({ "success": False, "message": result["message"]})
    except Exception as e:
        return JSONResponse({ "success": False, "message": f"Error: {e}"})
    
