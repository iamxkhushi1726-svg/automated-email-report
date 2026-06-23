import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()


def send_report_email(html_content, recipient_email=None):
    """
    Send the HTML report as an email using Gmail SMTP.
    Credentials are loaded from .env file — never hardcoded.
    """
    sender_email = os.getenv("EMAIL_SENDER")
    sender_password = os.getenv("EMAIL_PASSWORD")
    recipient = recipient_email or os.getenv("EMAIL_RECIPIENT")

    if not all([sender_email, sender_password, recipient]):
        print("  [ERROR] Missing email credentials in .env file.")
        print("  Create a .env file with EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECIPIENT")
        return False

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "📊 Daily Sales Report — Automated"
    msg["From"] = sender_email
    msg["To"] = recipient

    part = MIMEText(html_content, "html")
    msg.attach(part)

    try:
        print(f"  Connecting to Gmail SMTP...")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient, msg.as_string())
        print(f"  [SUCCESS] Report sent to {recipient}")
        return True
    except smtplib.SMTPAuthenticationError:
        print("  [AUTH ERROR] Check your EMAIL_SENDER and EMAIL_PASSWORD in .env")
        print("  Gmail requires an App Password, not your regular password.")
        print("  Go to: myaccount.google.com/apppasswords")
        return False
    except smtplib.SMTPException as e:
        print(f"  [SMTP ERROR] {e}")
        return False
    except Exception as e:
        print(f"  [ERROR] {e}")
        return False