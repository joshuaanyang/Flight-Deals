from twilio.rest import Client

TWILIO_SID = 'TWILIO SID'
TWILIO_AUTH_TOKEN = 'TWILIO AUTH'
TWILIO_VIRTUAL_NUMBER = 'TWILIO NUMBER'
TWILIO_VERIFIED_NUMBER = 'NUMBER'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            messaging_service_sid=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
