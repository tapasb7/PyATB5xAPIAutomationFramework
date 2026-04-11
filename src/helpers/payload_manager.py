# Payloads

# Create Booking
# Update Booking
# Auth - Token

import os
from dotenv import load_dotenv

def payload_create_booking():
    payload = {
        "firstname": "Rogan",
        "lastname": "Josh",
        "totalprice": 112,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_update_booking():
    payload = {
        "firstname": "Monty",
        "lastname": "Singh",
        "totalprice": 1121,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2026-02-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_create_token():
    load_dotenv(override=True)
    payload = {
        'username': os.getenv('TOKEN_PAYLOAD_USERNAME'),
        'password': os.getenv('TOKEN_PAYLOAD_PASSWORD'),
    }
    return payload


