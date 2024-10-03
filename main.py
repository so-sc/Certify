# (c) 2022-2023, Akkil M G (https://github.com/HeimanPictures)
# License: GNU General Public License v3.0

"""
main.py
This module initializes the FastAPI application for the 'certify' service,
which generates and stores certificates for SOSC events.
"""

import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from router import api_router

app = FastAPI(
    title="certify",
    description=(
        "This is an application as a service to generate and store "
        "certificate for SOSC Events."
    ),
    version="0.0.2",
    contact={
        "name": "Akkil M G",
        "url": "http://github.com/AkkilMG",
    },
    license_info={
        "name": "GNU GENERAL PUBLIC License v3.0",
        "url": "https://www.gnu.org/licenses/gpl-3.0.en.html",
    },
    docs_url="/method",
    redoc_url="/",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    """Return a JSON response indicating the server is running successfully."""
    return JSONResponse({"success": True})

app.include_router(api_router.router, prefix="/api/v1")

if __name__ == "__main__":
    try:
        print('------------------- Initializing Web Server -------------------')
        print('----------------------- Service Started -----------------------')
        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    except KeyboardInterrupt:
        print('----------------------- Service Stopped -----------------------')

# No pointless strings should remain here
