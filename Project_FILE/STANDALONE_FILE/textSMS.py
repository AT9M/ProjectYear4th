from twilio.rest import Client

account_sid ="AC6a6f62dbaf928dab9d849e25d1412efb" # Put your Twilio account SID here

auth_token ="25380b677c458cbfca4abc0eea9bdce0" # Put your auth token here

client = Client(account_sid, auth_token)

message = client.api.account.messages.create(

to="+33617966728", # Put your cellphone number here

from_="+447588675953", # Put your Twilio number here

body="#Whatever you want")
