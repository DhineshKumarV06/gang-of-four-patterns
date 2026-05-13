# Notification factory

from abc import ABC, abstractmethod

#product interfere
class notification(ABC):
    def send(self,message):
        pass

#concrete products
class EmailNotification(notification):
    def send(self,message):
        print(f"sending messages :{message}")

class SMSNotification(notification):
    def send(self,message):
        print(f"sending messages :{message}")

# factory
class notificationFactory:

    @staticmethod
    def create_notifi(notification_type):
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "SMS":
            return SMSNotification()
        else:
            raise ValueError ("invalid notification type")
notification = notificationFactory.create_notifi("email")
notification.send("Vanakam")