from abc import ABC, abstractmethod


class EmailSender(ABC):
    @abstractmethod
    def send_email(self, recipient: str, subject: str, body: str, html: bool = False):
        pass
