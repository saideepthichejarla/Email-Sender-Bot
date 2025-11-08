import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


sender_email = "saideepthichejarla2026@gmail.com"
app_password = "ahyffcxzguxoqtjp"  
receiver_email = "lakshminaga6119@gmail.com"


subject = "Test Email"
body = "This is a test email sent successfully from Python!"


message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

message.attach(MIMEText(body, "plain"))

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email sent successfully!")