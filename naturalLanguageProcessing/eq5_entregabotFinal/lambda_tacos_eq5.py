import json
import random
import requests

def lambda_handler(event, context):

    intent_name = event['interpretations'][0]['intent']['name']
    slots = event['interpretations'][0]['intent']['slots']
    message = "Su pedido fue:\n"
    
    if slots['Alambres'] != None:
        message = message + "-Alambre de " + slots['Alambres']['value']['interpretedValue'] + "\n"
        
    if slots['Costras'] != None:
        message = message + "-Costra de " + slots['Costras']['value']['interpretedValue'] + "\n"
        
    if slots['Volcanes'] != None:
        message = message + "-Volcán de " + slots['Volcanes']['value']['interpretedValue'] + "\n"
        
    if slots['Tortas'] != None:
        message = message + "-Torta de " + slots['Tortas']['value']['interpretedValue'] + "\n"
        
    if slots['Bebidas'] != None:
        message = message + "-Bebida es " + slots['Bebidas']['value']['interpretedValue'] + "\n"
        
    if slots['Postres']!= None:
        message = message + "-Postre es " + slots['Postres']['value']['interpretedValue'] + "\n"
        
    

    response = {
       'sessionState' : {
            'dialogAction' : {
                'type' : 'Close'
            },
            'intent' : {
                'name' : intent_name,
                'state' : 'Fulfilled'
            }
       },
        'messages': [
             {
                'contentType' : 'PlainText',
                'content' : message
             }
        ]
    }

    return response
