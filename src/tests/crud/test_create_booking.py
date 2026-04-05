import pytest
import allure
import logging #use to print logs

from src.helpers.api_requests_wrapper import post_request
from src.constants.api_constants import ApiConstants
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import *
from src.utils.utils import Utils

class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title('Verify that Create Booking status and Booking ID should not be NULL')
    @allure.description(
        "Creating a Booking from the payload and verify that booking id should not be null and status code should be 200 for the correct payload")
    def test_create_booking_positive(self):
        LOGGER= logging.getLogger(__name__)
        LOGGER.info("Starting of Testcase")
        response = post_request(
            url= ApiConstants().usrl_create_booking(),
            auth= None,
            headers= Utils().common_headers_json(),
            payload= payload_create_booking(),
            in_json= False)
        LOGGER.info('POST Req Done')
        LOGGER.info('Now Verify')
        verify_http_status_code(response_data= response, expected_data=200)
        LOGGER.info(response.json())
        LOGGER.info(response.json()['bookingid'])
        verify_json_key_not_null(response.json()['bookingid'])
        verify_json_key_greater_than_zero(response.json()['bookingid'])


    @pytest.mark.negative
    @allure.title('Verify that Create Booking with empty payload')
    @allure.description(
        "Creating a Booking invalid, verify status code 500 for the incorrect payload")
    def test_create_booking_negative_tc1(self):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("Starting of Testcase")
        response = post_request(
            url=ApiConstants().usrl_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload={},
            in_json=False)
        LOGGER.info('POST Req Done')
        LOGGER.info('Now Verify')
        verify_http_status_code(response_data=response, expected_data=500)

    @pytest.mark.negative
    @allure.title('Verify that Create Booking with empty payload')
    @allure.description(
        "Creating a Booking invalid, verify status code 500 for the incorrect payload")
    def test_create_booking_negative_tc2(self):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("Starting of Testcase")
        response = post_request(
            url=ApiConstants().usrl_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload={'name' : 'Tapas'},
            in_json=False)
        LOGGER.info('POST Req Done')
        LOGGER.info('Now Verify')
        verify_http_status_code(response_data=response, expected_data=500)




