import requests as requests


def load_random_word():
    path = 'https://jsonkeeper.com/b/7SGM'

    response = requests.get(path)
    response_json = response.json()
    print(response_json)

load_random_word()
