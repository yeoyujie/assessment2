import requests


def lambda_handler(event, context):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    return response.json()
