from random import randint
import requests

BASE_URL = 'https://simple-books-api.glitch.me/api-clients'


def login(clientName=None, clientEmail=None):
    json = {
        'clientName': clientName,
        'clientEmail': clientEmail
    }
    response = requests.post(BASE_URL, json=json)
    return response


def get_token():
    nr = randint(1, 9999999)
    json = {
        'clientName': 'Test',
        'clientEmail': f'valid_emailTEs{nr}@mailinator.com'
    }
    response = requests.post(BASE_URL, json=json)
    return response.json()['accessToken']
