from twilio.rest import Client  # You will need to install this package.

class Text:
    def __init__(self):
        self.weather_message = "place holder"  # it can be anything, because text.weather_message will be changed in the main.py
        self.account_sid = "YOUR TWILIO ID"
        self.auth_token = "YOUR TWILIO TOKEN"

    def weather_text(self):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
            .create(
            body=self.weather_message,
            from_='+1 YOUR TWILIO NUMBER',  # the numbers will need to be this format: "+11234567890"
            to='+1 YOUR NUMBER',
        )

        print(message.status)

    def puppy_text(self):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
            .create(
            body="Hang out with the dog!",
            from_='+1 YOUR TWILIO NUMBER',
            to='+1 YOUR NUMBER',
        )

        print(message.status)
