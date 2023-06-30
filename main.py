import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

from services import sub_text_in_template, get_email_lists

message = MIMEMultipart()

text = sub_text_in_template(examle='Wold')
html_part = MIMEText(text, 'html')
message.attach(html_part)

message['From'] = 'exampleEmail'
message['Subject'] = 'ExampleMassage'

smtp_server = 'smtp.gmail.com'
smpt_port = 587
smtp_username = 'ExampleUsername'
smtp_password = 'ExamplePassword'      # if you using gmail, you need app-password

emails = get_email_lists()
for email in emails:
    message['To'] = email
    with smtplib.SMTP(smtp_server, smpt_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(message)
