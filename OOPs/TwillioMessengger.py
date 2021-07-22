from twilio.rest import Client

account_sid = ''
auth_token = ''

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18322934969",
    from_="+18322934969",
    body="Hello!"
)

print(message.sid)