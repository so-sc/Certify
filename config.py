"""
This module handles the configuration settings for the Certify project.
It loads environment variables from a .env file and sets up email credentials 
and template configurations.
"""
import os
from dotenv import load_dotenv

load_dotenv()


Template = {
    1: "test" # file name without extension (Add template to './templates')
}


# Mail
email = os.getenv("email")
password = os.getenv("password")
