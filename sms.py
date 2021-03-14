# Isaac Smith
# isaack.bsmith@gmail.com
# re-wrote the code for bulk sms api to support python3

import urllib.request as urlreq
import urllib3


def send_sms(api_key,phone,message,sender_id):

    #parameters to send SMS
    params = {"key":api_key,"to":phone,"msg":message,"sender_id":sender_id}

    #url to send SMS
    # /*******************API URL FOR SENDING MESSAGES********/
    url = 'http://clientlogin.bulksmsgh.com/smsapi?'+ urllib3.request.urlencode(params)

    # /****************API URL TO CHECK BALANCE****************/
    # url = 'http://clientlogin.bulksmsgh.com/api/smsapibalance?'+ urllib3.request.urlencode(api_key)

    http = urllib3.PoolManager()
    content = http.request('POST', url)
    response = content.data.decode('utf-8')

    print(response)

    #Interpreting codes obtained from reading the URL
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

#Defining variables to be used inside function
api_key = 'd7368b3e63a0c0902b6f' #API Key generated from your mNotify account
phone = '0276679293' #SMS recepient's phone number
message = 'status check' #Message to be sent
sender_id = 'Drwp' #Sender id for the message


#Calling function that was created to send sms
send_sms(api_key,phone, message, sender_id)