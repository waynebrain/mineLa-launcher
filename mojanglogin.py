import requests
import json

def loginintomc(username , password):
    url = "https://authserver.mojang.com/authenticate"

    payload = {
            "agent": {              
                    "name": "Minecraft",
                    "version": 1
                },
            "username": username,

            "password": password,
            }

    headers={'content-type' , 'application/json'}

    response = requests.post(url , data=json.dumps(payload))
    return response.content
