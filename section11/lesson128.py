from email.mime import multipart
from email.mime import text
import smtplib

smtp_host = "smtp.gmail.com"
smtp_port = 587
from_email = "from@gmail.com"
to_email = "to@gmail.com"
username = "username"
password = "password"

message = multipart.MIMEMultipart()
message["Subject"] = "subject"
message["From"] = from_email
message["To"] = to_email
message.attach(text.MIMEText("content", "plain"))
with open("section11/log_test.log", "r") as f:
    attachment = text.MIMEText(f.read(), "plain")
    attachment.add_header(
        "Content-Disposition", "attachment",
        filename="log_test.log"
    )
    message.attach(attachment)

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(message)
server.quit()
