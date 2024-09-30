import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(body_data):
	# Email configuration
	smtp_server = 'mail.nike.com'
	smtp_port = 587
	username = 'artyom.pak@nike.com' # << Sending E-mail Account
	password = '_Dftyv3y9hy09' # << PW for the Sending E-mail Account

	# Create the email
	sender_email = username
	#receiver_email = 'mike.pandel@nike.com,Artyom.Pak@nike.com' # Replace with the recipient's email
	receiver_email = [
    'Artyom.Pak@nike.com',
	]
	subject = 'RITM3355837 | TASK4014435 - Testing w/Importance'
	body = body_data

	# Create a multipart email
	msg = MIMEMultipart()
	msg['From'] = username
	#sg['To'] = receiver_email
	msg['To'] = ', '.join(receiver_email)  # Join the list of recipients into a single string
	msg['Subject'] = subject
	msg['X-Priority'] = '2' # 1 (Highest), 2 (High), 3 (Normal), 4 (Low), 5 (Lowest). 3 (Normal) is default if the field is omitted.

	# Attach the email body
	msg.attach(MIMEText(body, 'plain'))

	# Send the email
	try:
	    with smtplib.SMTP(smtp_server, smtp_port) as server:
	        server.starttls() # Upgrade the connection to a secure encrypted SSL/TLS connection
	        server.login(username, password) # Log in to your email account
	        server.sendmail(sender_email, receiver_email, msg.as_string()) # Send the email
	    print("Email sent successfully!")
	except Exception as e:
	    print(f"Failed to send email: {e}")

def test_alert():
    """
    test
    """
    result = "RITM3355837\nAutomated test alert from Mike and Art. "
    return result


if __name__ == "__main__":
    send_email(test_alert())
  
