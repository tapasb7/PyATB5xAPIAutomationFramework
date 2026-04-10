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

def put_request(url,auth, headers, payload, in_json):
    put_response_data= requests.put(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json:
        return put_response_data.json()
    else:
        return put_response_data

def patch_request(url,auth, headers, payload, in_json):
    patch_request_data = requests.patch(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json:
        return patch_request_data.json()
    else:
        return patch_request_data


def delete_request(url,auth, headers, in_json):
    delete_response_data = requests.delete(url=url, auth=auth, headers=headers)
    if in_json:
        return delete_response_data.json()
    else:
        return delete_response_data
