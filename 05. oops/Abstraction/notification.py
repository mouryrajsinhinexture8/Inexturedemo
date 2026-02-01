from abc import ABC, abstractmethod

# Interface equivalent
class NotificationSender(ABC):

    @abstractmethod
    def send(self, to, message):
        pass


# Email implementation
class EmailSender(NotificationSender):

    def send(self, to, message):
        print(f"Email sent to {to}: {message}")


# SMS implementation
class SmsSender(NotificationSender):

    def send(self, to, message):
        print(f"SMS sent to {to}: {message}")


# Service class 
class AlertService:

    def __init__(self, sender: NotificationSender):
        self.sender = sender

    def send_alert(self, to, message):
        self.sender.send(to, message)


# Main execution
if __name__ == "__main__":

    email = EmailSender()
    email_alert = AlertService(email)
    email_alert.send_alert("mouryrajjadeja@gmail.com", "Hello email")

    sms = SmsSender()
    sms_alert = AlertService(sms)
    sms_alert.send_alert("Jadeja888", "Hello sms")
