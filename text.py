from twilio.rest import Client

class Text:
    def __init__(self):
        self.weather_message = "test"
        self.account_sid = "ACb1fabd138d7f5575bb001c4712bd4f1d"
        self.auth_token = "e119420d47ae634aa954e21e850e0974"

    def weather_text(self):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
            .create(
            body=self.weather_message,
            from_='+15172012350',
            to='+1YOUR NUMBER',
        )

        print(message.status)

    def puppy_text(self):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
            .create(
            body="Hang out with the dog!",
            from_='+15172012350',
            to='+1YOUR NUMBER',
        )

        print(message.status)