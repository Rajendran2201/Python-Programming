import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email and password for the sender
sender_email = "anu@aalam.io"
password = "******"
# Email addresses for the sender and recipient
sender = "anu@aalam.io"
recipient = "karthiga.m@cit.edu.in"


# Create a message object
message = MIMEMultipart()

message["From"] = sender
message["To"] = recipient
message["Subject"] = "Test Email"

# Email body
body = "This is a test email sent from Python."
message.attach(MIMEText(body, "plain"))

# Connect to the SMTP server
with smtplib.SMTP("smtp.zoho.com", 587) as server:
  server.starttls()
  print("Logging in to the SMTP server")
  server.login(sender_email, password)
  print("Logged in to the SMTP server")
  server.sendmail(sender_email, recipient, message.as_string())

print("Email sent successfully!")