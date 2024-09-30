import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(body_data):
    """
    
    """
    # Email configuration
    username = 'blabla.com'  # << Sending E-mail Account
    password = 'XxXxXx'  # << PW for the Sending E-mail Account
    smtp_server = 'mail.YOURDOMAIN.com' # nike
    smtp_port = 587

    # Create the email
    sender_email = username
    receiver_email = ['blabla@bla.com', '']
    subject = 'RITM3355837 | TASK4014435 - Testing w/Importance'
    body = body_data

    # Create a multipart email
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = ', '.join(receiver_email)  # Join the list of recipients into a single string
    msg['Subject'] = subject
    msg['X-Priority'] = '2'  # 1 (Highest), 2 (High), 3 (Normal), 4 (Low), 5 (Lowest)

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(username, password)  # Log in to your email account
            server.sendmail(sender_email, receiver_email, msg.as_string())  # Send the email
        print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    send_email('test')
