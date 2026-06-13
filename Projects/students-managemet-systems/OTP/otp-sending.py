# w.r.t program to create otp sending on mobile number app using python
# install all dependencies
# pip install twilio    
# import all dependencies

import requests
import random

#create a 6 to 7 digit random otp 
otp=random.randint(100000,999999)

#send otp om that numbers that can not be in DND 
mobile=9998003879

#applied thrid party integration twilio | way2sms | fast2sms etc
url =""

payload = {
    "route" : "otp",
    "variable_values" : f"{otp}",
    "numbers" : f"{mobile}"
}

headers= {
    "authorization" : ""
}

# get response of sms API via fast2sms

response=requests.post('url', data=payload, headers=headers)
print("OTP IS GENERATED SUCCESSFULLY",otp)
print("response.text")