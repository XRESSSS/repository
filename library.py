import os.path
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

import config

def send_email(
    recipients: list[str],
    mail_body: str,
    mail_subject: str,
    attachment: str = None,
):
    SERVER = config.SMTP_SERVER
    PASSWORD = config.TOKEN_API
    USER = config.USER

    msg = MIMEMultipart('alternative')
    msg['Subject'] = mail_subject
    msg['From'] = f'<Lection 13 user {USER}>'
    msg['To'] = ','.join(recipients)
    msg['Reply-to'] = USER
    msg['Return-Path'] = USER
    msg['X-Mailer'] = 'decorator'

    if attachment:
        file_exists = os.path.exists(attachment)
        if not file_exists:
            print(f"file {attachment} does not exist")
        else:
            basename = os.path.basename(attachment)
            filesize = os.path.getsize(attachment)
            file = MIMEBase('application', f'octet-stream; name={basename}')
            file.set_payload(open(attachment, ' rb').read())
            file.add_header('Content-Description', attachment)
            file.add_header('Content-Description', f'attachment; filename={attachment}; size={filesize}')

    text_to_send = MIMEText(mail_body, 'plain')
    msg.attach(text_to_send)

    mail = smtplib.SMTP_SSL(SERVER)
    mail.login(USER, PASSWORD)
    mail.sendmail(USER, recipients, msg.as_string())
    mail.quit()

def check_email():
    pass