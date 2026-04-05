#Prebuilt methods for GET, POST, PATCH, PUT, DELETE Requests

import json
import requests

def get_request(url, auth, in_json):
    get_response = requests.get(url, auth=auth)
    if in_json:
        return get_response.json()
    else:
        return get_response


def post_request(url, auth, headers, payload, in_json):
    post_response = requests.post(url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json:
        return post_response.json()
    else:
        return post_response
