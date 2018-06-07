from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC16b867966eb834aa3454af4dfe38a28c"
# Your Auth Token from twilio.com/console
auth_token  = "d5609aa83ac7af01ca7147f475649ecd"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16196746220", 
    from_="+17608402724",
    body="My name is Haeun Kim?")

print(message.sid)
