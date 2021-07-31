# importing necessary libraries
from twilio.rest import Client
import os
import math
import random

# putting necessary information regarding twilio account
account_sid = 'ACCOUNT_SID'
auth_token = 'AUTH_TOKEN'
client = Client(account_sid, auth_token)

# generating random otp
digits = "0123456789"
OTP = ""
for i in range(6):
    OTP += digits[math.floor(random.random() * 10)]
otp = OTP
msg = otp + " is your OTP"

# getting number to sent otp
num_to_send = input("Enter number to send OTP: ")

message = client.messages.create(
    body=msg,
    from_="+12314987140",
    to=num_to_send
)

# getting response in case of successful sms
print(message.sid)
flag = 0
while flag != 1:
    rslt = input("Enter your OTP: ")

    # verifying OTP
    if rslt == otp:
        print("OTP verified successfully")
        flag = 1
    else:
        print("Please check your OTP & try again")
        flag = 0
