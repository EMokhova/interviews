import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


class Client:

    def __init__(self, login, password):
        login = login
        password = password

    def send_email(self, recipients, server, port, subject, message):
        email = MIMEMultipart()
        email['From'] = self.login
        email['To'] = ', '.join(recipients)
        email['Subject'] = subject
        email.attach(MIMEText(message))
        sendemail = smtplib.SMTP(server, port)
        sendemail.ehlo()
        sendemail.starttls()
        sendemail.ehlo()
        sendemail.login(self.login, self.password)
        sendemail.sendmail(self.login, sendemail, email.as_string())
        sendemail.quit()

    def recieve_email(self, server, folder, header=None):
        recieve_mail = imaplib.IMAP4_SSL(server)
        recieve_mail.login(self.login, self.password)
        recieve_mail.list()
        recieve_mail.select(folder)
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = recieve_mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = recieve_mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        result_recieve = email.message_from_string(raw_email)
        recieve_mail.logout()
        return result_recieve


if __name__ == '__main__':
    gmail = Client('login@gmail.com', 'qwerty')
    gmail.sendmail('smtp.gmail.com', 587,'Subject', ['vasya@email.com', 'petya@email.com'], 'Message'))
    gmail.receive_mail('imap.gmail.com', 'inbox')


