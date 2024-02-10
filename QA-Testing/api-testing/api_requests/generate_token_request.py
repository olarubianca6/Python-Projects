from random import randint

import requests

BASE_URL = "https://simple-books-api.glitch.me"
API_CLIENTS_ENDPOINT = "/api-clients"

def get_token():
    token_found = False
    response = None

    while not token_found:
        random_number = randint(1, 999999999999999999)
        request_body = {
            "clientName": "Python",
            "clientEmail": f"pyta{random_number}@google.com"
        }
        response = requests.post(BASE_URL + API_CLIENTS_ENDPOINT, json=request_body)
        if "accessToken" in response.json().keys():
            token_found = True

    return response.json()['accessToken']