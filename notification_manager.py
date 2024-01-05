import smtplib
from twilio.rest import Client

TWILIO_SID = "AC35908559e4b634d2c2eb2339747e67f8OIUYB345"
TWILIO_AUTH_TOKEN = "bc650a0f79c5b3b47551fcb1a26537d00OKJ21"
TWILIO_VIRTUAL_NUMBER = "+11007700142440"
TWILIO_VERIFIED_NUMBER = "+1907597044364"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login('obiagerichinwej@gmail.com','whje qxzz ckdi hmjf')
            for email in emails:
                connection.sendmail(
                    from_addr='obiagerichinwej@gmail.com',
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )