
from dotenv import load_dotenv
import os

load_dotenv()


Template = {
    1: "test" # file name without extension (Add template to './templates')
}


# Mail
email = os.getenv("email")
password = os.getenv("password")
