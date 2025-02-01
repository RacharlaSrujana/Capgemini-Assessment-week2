'''Implement method overriding for a `Notification` class where `send()` is overridden in `EmailNotification` and `SMSNotification`.'''

class Notification:
    def send(self):
        print("Message can be send using email,sms")
class EmailNotification(Notification):
    def send(self):
        print("Email notification has been sent to abc@gmail.com")
class SMSNotification(Notification):
    def send(self):
        print("SMS has been sent to 9078563412")
def myFunction(obj):
    obj.send()
notification=Notification()
myFunction(notification)
email=EmailNotification()
myFunction(email)
sms=SMSNotification()
myFunction(sms)