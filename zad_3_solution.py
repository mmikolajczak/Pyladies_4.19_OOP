from zad_1_solution import Person
from email_sender import GmailEmailSender
import datetime  # importujemy potrzebne klasy/funkcjonalności z odpowiednich modułów


class BirthdayWishesSender(GmailEmailSender):  # tworzymy klasę, dziedziczącą po naszym EmailSenderze

    def generate_message_content(self, person):  # i nadpisujemy metody abstrakcyjne
        is_female = person.name[-1] == 'a'  # sprawdzamy według końcówki imienia, czy mamy do czynienia z kobietą czy mężczyzną
        return f'Drog{"a" if is_female else "i"} {person.name},\n spóźnione wszystkiego najlepszego z okazji' \
               f' twoich {person.age()} urodzin.'  # tworzymy treść wiadomości zgodnie z treścią zadania (f-stringiem)


receiver = Person('Imię', 'Nazwisko', datetime.date(2000, 1, 1))
receiver_address = 'jakiś_email@jakaś_domena.com'
gmail_user = 'zbyszek.nowak.fejkmejl@gmail.com'  # konto stworzone na potrzebę zajęć - ale nie krępuj się i użyj własnego
                                                 # jeśli tylko masz ochotę (instrukcje konfiguracyjne są w slajdach)
gmail_pass = 'Pyladies2018'
mail_sender = BirthdayWishesSender(gmail_user, gmail_pass)  # tworzymy obiekt naszej nowej klasy
mail_sender.send_mail(receiver_address, receiver)  # i wysyłamy maila odpowiednią metodą
