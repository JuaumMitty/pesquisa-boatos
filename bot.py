from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

# chatbot logic
def bot():
 
    # user input
    user_msg = request.values.get('Body', '').lower()
 
    # creating object of MessagingResponse
    response = MessagingResponse()
 
    # User Query
    q = user_msg + "geeksforgeeks.org"
 
    # list to store urls
    result = []
 
    # searching and storing urls
    for i in search(q, tld='co.in', num=6, stop=6, pause=2):
        result.append(i)
 
    # displaying result
    # msg = response.message(f"--- Result for '{user_msg}' are  ---")
 
    # msg = response.message(result[0])
    # msg = response.message(result[1])
    # msg = response.message(result[2])
    # msg = response.message(result[3])
    # msg = response.message(result[4])
 
    return str('Funcionando')




























# from twilio.rest import Client, MessagingResponse
 
# account_sid = 'AC4634c3584e3904a7ebea9be1f9c779d4' 
# auth_token = '8521ef2ccbc5e148036e426a1e252321' 
# client = Client(account_sid, auth_token) 
 
# message = client.messages.create( 
#                               from_='whatsapp:+14155238886',  
#                               body='Your appointment is coming up on July 21 at 3PM',      
#                               to='whatsapp:+556198260268' 
#                           ) 
 

# test = client.MessagingResponse('body', '')
# print(test.lower())
# print(message.sid)










 
# account_sid = 'AC4634c3584e3904a7ebea9be1f9c779d4' 
# auth_token = '8521ef2ccbc5e148036e426a1e252321' 
# client = Client(account_sid, auth_token) 
 
# message = client.messages.create( 
#                               from_='whatsapp:+14155238886',  
#                               body='My master said: Hi',      
#                               to='whatsapp:+556195160239' 
#                           ) 
 
# print(message.sid)