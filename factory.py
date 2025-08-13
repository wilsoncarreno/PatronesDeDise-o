from abc import ABC, abstractmethod

# 1️⃣ Product interface
class Messenger(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

# 2️⃣ Concrete products
class EmailMessenger(Messenger):
    def send(self, message: str):
        print(f"📧 Sending Email: {message}")

class SMSMessenger(Messenger):
    def send(self, message: str):
        print(f"📱 Sending SMS: {message}")

class WhatsAppMessenger(Messenger):
    def send(self, message: str):
        print(f"💬 Sending WhatsApp: {message}")

# 3️⃣ Creator (abstract)
class Notifier(ABC):
    @abstractmethod
    def create_messenger(self) -> Messenger:
        pass

    def notify(self, message: str):
        messenger = self.create_messenger()
        messenger.send(message)

# 4️⃣ Concrete creators
class EmailNotifier(Notifier):
    def create_messenger(self) -> Messenger:
        return EmailMessenger()

class SMSNotifier(Notifier):
    def create_messenger(self) -> Messenger:
        return SMSMessenger()

class WhatsAppNotifier(Notifier):
    def create_messenger(self) -> Messenger:
        return WhatsAppMessenger()

# 5️⃣ Client code
if __name__ == "__main__":
    notifier1 = EmailNotifier()
    notifier1.notify("Hello, this is an important message.")

    notifier2 = SMSNotifier()
    notifier2.notify("Your code is 1234.")

    notifier3 = WhatsAppNotifier()
    notifier3.notify("Meeting at 3 PM.")
