#Smart mail transfer protocol
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
otp = random.randint(1111,9999)

smtp_server = "smtp.gmail.com"
smtp_port = 587
mailusername = "pasthamsairam42@gmail.com"
mailpassword = "yusq hmuj ceyv lezz"

from_email = "pasthamsairam42@gmail.com"
to_email = input("Enter Email Address: ")
subject = "OTP For Validation"
body = f"Otp for Validation is {otp}"

msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['subject'] = subject
msg.attach(MIMEText(body,'plain'))

server = smtplib.SMTP(smtp_server,smtp_port)
server.starttls()
server.login(mailusername,mailpassword)
server.send_message(msg)
server.quit()

verifyotp = int(input("enter Otp to Verify: "))
if verifyotp == otp:
    print("Login Sucess")
else:
    print("Login Failed")

