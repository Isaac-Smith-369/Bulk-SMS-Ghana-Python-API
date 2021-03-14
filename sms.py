# email: isaack.bsmith@gmail.com
# github: https://github.com/Isaac-Smith-369
# Bulk SMS API - python3


import urllib3


def send_sms(api_key,phone,message,sender_id):

    # parameters to send SMS
    params = {"key":api_key,"to":phone,"msg":message,"sender_id":sender_id}

    # url to send SMS
    # /*******************API URL FOR SENDING MESSAGES********/
    url = 'http://clientlogin.bulksmsgh.com/smsapi?'+ urllib3.request.urlencode(params)

    # /****************API URL TO CHECK BALANCE****************/
    bal_url = 'http://clientlogin.bulksmsgh.com/api/smsapibalance?'+ urllib3.request.urlencode(api_key)

    # We create a PoolManager to generate a request.
    # It handles all of the details of connection pooling and thread safety.
    http = urllib3.PoolManager()

    # We generate a POST request.
    content = http.request('POST', url)

    # We get the data or the response and decode it into text.
    response = content.data.decode('utf-8')
    

    # Interpreting codes obtained from reading the URL
    if response == '1000':
        print("Message successfully sent")
    elif response == '1002':
        print("Message not sent")
    elif response == '1003':
        print("Your balance is not enough")
    elif response == '1004':
        print("Invalid API Key")
    elif response == '1005':
        print("Phone number not valid")
    elif response == '1006':
        print("Invalid sender id")
    elif response == '1008':
        print("Empty message")

# Defining variables to be used inside function
api_key = 'xxxxxxxxxxxxxx' #API Key generated from your mNotify account
phone = '0213456789' #SMS recepient's phone number
message = 'message' #Message to be sent
sender_id = 'BulkSMS' #Sender id for the message


# Calling function that was created to send sms
send_sms(api_key, phone, message, sender_id)
