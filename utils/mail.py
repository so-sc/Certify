

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from config import email, password

def sendMail(name, mail, subject, body):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = email
    msg["To"] = mail
    html_part = MIMEText(body, "html")
    msg.attach(html_part)
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(email, password)
            server.sendmail(email, mail, msg.as_string())
            print("Email sent successfully!")
            return { "success": True, "message": "Email sent successfully" }
        return { "success": False, "message": "Failed to send email" }
    except Exception as e:
        print(f"Failed to send email: {e}")
        return { "success": False, "message": "Failed to send email" }
