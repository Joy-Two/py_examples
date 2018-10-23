from twilio.rest import Client

client = Client("XXX", "XXX")
client.messages.create(to="XXX", 
                       from_="XXX", 
                       body="Hello from Python")