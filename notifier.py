# notifier.py
import smtplib
from email.message import EmailMessage
from config import settings

def send_email(entry: dict) -> None:
    """
    Sends an email with the article title, link and summary.
    """
    msg = EmailMessage()
    msg['From']    = settings.smtp_user
    msg['To']      = settings.email_to
    msg['Subject']= f"AFR Equity Alert: {entry['title']}"
    body = (
        f"{entry['title']}\n\n"
        f"Link: {entry['link']}\n\n"
        f"{entry['summary']}"
    )
    msg.set_content(body)

    with smtplib.SMTP(settings.smtp_server, settings.smtp_port, timeout=10) as smtp:
        smtp.starttls()
        smtp.login(settings.smtp_user, settings.smtp_pass)
        smtp.send_message(msg)