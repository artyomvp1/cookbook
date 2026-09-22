import smtplib
from email.mime.text import MIMEText

# --- Configuration ---
SMTP_SERVER = "issmtp1.nike.com"
SMTP_PORT = 25
SENDER = "artyom.pak2@nike.com"
RECIPIENTS = ["artyomvp1@gmail.com", "artyom.pak2@nike.com"]
SUBJECT = "Intake form"
BODY = "test passed."

# --- Build message ---
msg = MIMEText(BODY)
msg["Subject"] = SUBJECT
msg["From"] = SENDER
msg["To"] = ", ".join(RECIPIENTS)

# --- Send ---
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30) as server:
        server.sendmail(SENDER, RECIPIENTS, msg.as_string())
    print(f"Email sent successfully to {len(RECIPIENTS)} recipient(s).")
except Exception as e:
    print(f"Failed to send email: {e}")
