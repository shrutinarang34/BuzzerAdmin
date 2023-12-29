import requests
api_url = "https://bapi.beeclue.com"

endpoints = {
    'login' : '/businesses/users/signin'
}

def post(endpoint: str, json: dict = None):
    return requests.post(api_url+endpoint, json = json)

