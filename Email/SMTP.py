from email.mime.text import MIMEText
import smtplib


class EmailSender:

    def TxtEmail(self):
        msg = MIMEText(
            'Hello, I have send this msg form Python', 'plain', 'utf-8')

    def send(self, fromAddr, fromPwd, toAddr, smtpServer):
        server = smtplib.SMTP(smtpServer, 25)


if __name__ == '__main__':
    emailSender = EmailSender()
