from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def notify(self, source, destination, message):
        pass

class SMSNotification(Notification):
    def notify(self, source, destination, message):
        print(f"Sending SMS from {source} to {destination}: {message}")

class WhatsAppNotification(Notification):
    def notify(self, source, destination, message):
        print(f"Sending WhatApp message from {source} to {destination}: {message}")

class EmailNotification(Notification):
    def notify(self, source, destination, message):
        print(f"Sending Email from {source} to {destination}: {message}")


class NotificationFactory:

    @staticmethod
    def create_notification(type):
        if type == "sms":
            return SMSNotification()
        elif type == "whatsapp":
            return WhatsAppNotification()
        elif type == "email":
            return EmailNotification()
        else:
            return None
        

if __name__ == "__main__":

    notification: Notification = NotificationFactory.create_notification("sms")
    if notification is None:
        print("Unsupported Notification")
    else:
        notification.notify("9876543210", "9123456780", "Hello")
