import smtplib
from abc import ABCMeta, abstractmethod


class GmailEmailSender(metaclass=ABCMeta):
    """Klasa, której obiekty służą do wysyłania wiadomości z poczty Gmail."""

    def __init__(self, gmail_username, gmail_password):
        self.gmail_username = gmail_username
        self.gmail_password = gmail_password

    @abstractmethod
    def generate_message_content(self, *args, **kwargs):
        """
        Metoda abstrakcyjna, którą należy zaimplementować w klasie dziedziczącej.
        Na podstawie przekazanych argumentów powinna generować string, będący treścią wiadomości.
        """
        raise NotImplemented()

    def send_mail(self, receiver_email_address, *args, **kwargs):
        try:
            self._initialize_smtp()
            email_content = self.generate_message_content(*args, **kwargs)
            self.server.sendmail(self.gmail_username, receiver_email_address, email_content.encode('utf-8'))
            self._terminate_smtp()
        except Exception:
            raise RuntimeError('Error during sending mail.')

    def _initialize_smtp(self):
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        self.server.ehlo()
        self.server.login(self.gmail_username, self.gmail_password)

    def _terminate_smtp(self):
        self.server.close()

