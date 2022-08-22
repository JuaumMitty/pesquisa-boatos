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
 
    return str('Funcionando')
