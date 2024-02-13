import json


def get_api_key():
    with open("/Users/Ivson/Documents/GitHub/chatbot/api_key/key.json") as api_key:
        key = json.load(api_key)
    return str(key['key'])
