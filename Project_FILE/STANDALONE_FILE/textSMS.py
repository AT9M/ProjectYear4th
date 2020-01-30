from twilio.rest import Client

account_sid ="You would like to know" # Put your Twilio account SID here

auth_token ="Still no" # Put your auth token here

client = Client(account_sid, auth_token)

message = client.api.account.messages.create(

to="+Do not call", # Put your cellphone number here

from_="+447588675953", # Put your Twilio number here

body="#Whatever you want")
