from email import message
import smtplib

smtp_host = "smtp.gmail.com"
smtp_port = 587
from_email = "from@gmail.com"
to_email = "to@gmail.com"
username = "username"
password = "password"

message = message.EmailMessage()
message.set_content("content")
message["Subject"] = "subject"
message["From"] = from_email
message["To"] = to_email

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(message)
server.quit()
