# (c) 2022-2023, Akkil M G (https://github.com/HeimanPictures)
# License: GNU General Public License v3.0

"""
This module defines the API routes for certificate generation and template upload.

Routes:
    /template: Handles the upload of a template file.
    /generate: Generates a certificate based on a template and user information.
    /generate-email: Generates an email and certificate based on a template and user details.
    /generate-url: Generates a certificate based on a URL, name, and ID.
    /generate-url-email: Generates an email and certificate based on a URL and user details.
"""

import requests
from fastapi import APIRouter, Request, UploadFile, File
from fastapi.responses import JSONResponse

from utils.gen_certificate import generate_certificate, generate_certificate_from_url

router = APIRouter()

@router.post("/template")
async def upload_template(file: UploadFile = File(...)):
    """
    Handles the upload of a template file and forwards it to an external service for processing.

    Args:
        file (UploadFile): The file to be uploaded.

    Returns:
        JSONResponse: A JSON response indicating the success or failure of the operation.
    """
    try:
        file_content = await file.read()
        response = requests.post(
            "https://certify.izaries.workers.dev/certificate",
            files={'file': (
                'certificate.pptx', file_content, 
                'application/vnd.openxmlformats-officedocument.presentationml.presentation'
            )},
            timeout=10  # Added timeout
        ).json()
        if response["success"]:
            return JSONResponse({
                "success": True, 
                "dl": f"https://certify.izaries.workers.dev/download?id={response['id']}&ext=pptx"
            })
        return JSONResponse({"success": False, "message": response["message"]})
    except requests.exceptions.RequestException as e:
        return JSONResponse({"success": False, "message": f"Request Error: {e}"})
    except ValueError as e:
        return JSONResponse({"success": False, "message": f"JSON parsing error: {e}"})
    except Exception as e:
        return JSONResponse({"success": False, "message": f"Unexpected error: {e}"})


@router.post("/generate")
async def generate_certificate_route(template: int, name: str, user_id: str):
    """
    Generate a certificate based on the provided template and user information.

    Args:
        template (int): The template ID to be used for generating the certificate.
        name (str): The name of the individual for whom the certificate is generated.
        user_id (str): The ID of the individual.

    Returns:
        JSONResponse: A JSON response containing the success status and either the 
                      download link or an error message.
    """
    try:
        value = {"name": name, "id": user_id}
        result = generate_certificate(template, value)
        if result['success']:
            return JSONResponse({"success": True, 'dl': result['dl']})
        return JSONResponse({"success": False, "message": result["message"]})
    except ValueError as e:
        return JSONResponse({"success": False, "message": f"Value error: {e}"})
    except Exception as e:
        return JSONResponse({"success": False, "message": f"Unexpected error: {e}"})


@router.post("/generate-email")
async def generate_email_and_certificate(
    template: int, name: str, user_id: str, subject: str, body: str, email: str
):
    """
    Generates an email and certificate based on the provided template and user details.

    Args:
        template (int): The template ID to be used for generating the certificate.
        name (str): The name of the recipient.
        user_id (str): The ID of the recipient.
        subject (str): The subject of the email.
        body (str): The body content of the email.
        email (str): The recipient's email address.

    Returns:
        JSONResponse: A JSON response indicating the success or failure of the operation.
    """
    try:
        value = {"name": name, "id": user_id, "body": body, "subject": subject}
        result = generate_certificate(template, value, email=email)
        if result['success']:
            return JSONResponse({"success": True, 'dl': result['dl']})
        return JSONResponse({"success": False, "message": result["message"]})
    except ValueError as e:
        return JSONResponse({"success": False, "message": f"Value error: {e}"})
    except requests.exceptions.RequestException as e:
        return JSONResponse({"success": False, "message": f"Request Error: {e}"})
    except Exception as e:
        return JSONResponse({"success": False, "message": f"Unexpected error: {e}"})

@router.post("/generate-url")
async def generate_certificate_from_url_route(url: str, name: str, user_id: str):
    """
    Generates a certificate based on the provided URL, name, and ID.

    Args:
        url (str): The URL to fetch the certificate template.
        name (str): The name to be included in the certificate.
        user_id (str): The ID to be included in the certificate.

    Returns:
        JSONResponse: A JSON response indicating the success or failure of the operation.
    """
    try:
        value = {"name": name, "id": user_id}
        result = generate_certificate_from_url(url, value)
        if result['success']:
            return JSONResponse({"success": True, 'dl': result['dl']})
        return JSONResponse({"success": False, "message": result["message"]})
    except ValueError as e:
        return JSONResponse({"success": False, "message": f"Value error: {e}"})
    except Exception as e:
        return JSONResponse({"success": False, "message": f"Unexpected error: {e}"})


@router.post("/generate-url-email")
async def generate_email_and_certificate_from_url(
    url: str, name: str, user_id: str, subject: str, body: str, email: str
):
    """
    Generates an email and certificate based on the provided URL and user details.

    Args:
        url (str): The URL to generate the certificate from.
        name (str): The name of the recipient.
        user_id (str): The ID of the recipient.
        subject (str): The subject of the email.
        body (str): The body of the email.
        email (str): The email address to send the certificate to.

    Returns:
        JSONResponse: A JSON response indicating success or failure.
    """
    try:
        value = {"name": name, "id": user_id, "body": body, "subject": subject}
        result = generate_certificate_from_url(url, value, email=email)
        if result['success']:
            return JSONResponse({"success": True, 'dl': result['dl']})
        return JSONResponse({"success": False, "message": result["message"]})
    except ValueError as e:
        return JSONResponse({"success": False, "message": f"Value error: {e}"})
    except Exception as e:
        return JSONResponse({"success": False, "message": f"Unexpected error: {e}"})
