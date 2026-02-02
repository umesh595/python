class Notification:
    def send(self, message):
        raise NotImplementedError
class EmailNotification(Notification):
    def send(self, message):
        return f"Sent via Email: {message}"
class SMSNotification(Notification):
    def send(self, message):
        return f"Sent via SMS: {message}"
class PushNotification(Notification):
    def send(self, message):
        return f"Sent via Push: {message}"
notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]
for n in notifications:
    print(n.send("Hello"))