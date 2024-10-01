"""
Module for sending emails with attachments.
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import email, password

def send_email(recipient_email, subject, body):
    """
    Sends an email with the specified subject and body to the given recipient.

    Args:
        recipient_email (str): The email address of the recipient.
        subject (str): The subject of the email.
        body (str): The HTML body content of the email.
    Returns:
        dict: A dictionary containing the success status and a message.
              Example: { "success": True, "message": "Email sent successfully" }
    """
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = email
    msg["To"] = recipient_email
    html_part = MIMEText(body, "html")
    msg.attach(html_part)
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(email, password)
            server.sendmail(email, recipient_email, msg.as_string())
            print("Email sent successfully!")
            return {"success": True, "message": "Email sent successfully"}
    except smtplib.SMTPException as smtp_error:
        print(f"Failed to send email: {smtp_error}")
        return {"success": False, "message": "Failed to send email"}
    except ConnectionError as conn_error:
        print(f"Connection error: {conn_error}")
        return {"success": False, "message": "Failed to send email due to connection error"}
