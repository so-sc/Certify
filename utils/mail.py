

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import EMAIL, PASS

def sendEmail(name: str, email: str, result):
    try:
        html_content = f"""
        <html>
          <head></head>
          <body>
          {result}
          </body>
        </html>
        """
        message = MIMEMultipart()
        message["From"] = EMAIL
        message["To"] = email
        message["Subject"] = "SOSC: Certificate of Participation"
        message.attach(MIMEText(html_content, "html"))
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL, PASS)
        server.sendmail(EMAIL, email, message.as_string())
        server.quit()
        return {"success": True}
    except Exception:
        return {"success": False}