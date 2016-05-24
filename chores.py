from tinydb import TinyDB, Query
from twilio.rest import TwilioRestClient 
from datetime import datetime

# put your own credentials here 
ACCOUNT_SID = "AC340f4b294de9d112f03a87e9cd85bd7f" 
AUTH_TOKEN = "d4657b785d6eacbd320c57811c78e783" 
TWILIO_NUMBER = "4155790066" 

db = TinyDB('db.json')

def send_trash_reminder(phone_number):
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	client.messages.create(
		to=phone_number, 
		from_=TWILIO_NUMBER, 
		body="RV Trash reminder: Trash needs to go out tonight!",
	)


print "THIS HERE"

