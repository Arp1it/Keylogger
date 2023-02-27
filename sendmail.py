import smtplib

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)

email = "abc@gmail.com"
password = "234yourpassword"
message = "hello arpit"
send_mail(email, password, message)