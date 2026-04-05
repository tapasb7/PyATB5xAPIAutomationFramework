import pytest
import allure
import logging #use to print logs

from src.helpers.api_requests_wrapper import post_request
from src.constants.api_constants import ApiConstants
from src.helpers.payload_manager import *
from src.helpers.common_verification import *
from src.utils.utils import Utils
from dotenv import load_dotenv

class TestCreateToken(object):

    @pytest.mark.positive
    @allure.title('Verify that Create Booking status and Booking ID should not be NULL')
    @allure.description(
        "Creating a Booking from the payload and verify that booking id should not be null and status code should be 200 for the correct payload")
    def test_create_token_positive(self):
        LOGGER= logging.getLogger(__name__)
        LOGGER.info("Starting of Testcase")
        response = post_request(
            url= ApiConstants().url_create_token(),
            auth= None,
            headers= Utils().common_headers_json(),
            payload= payload_create_token(),
            in_json= False)
        LOGGER.info('POST Req Done')
        LOGGER.info('Now Verify')
        verify_http_status_code(response_data= response, expected_data=200)
        LOGGER.info(response.json())
        # print(response.json())
        LOGGER.info(response.json()['token'])
        verify_json_key_not_none(response.json()['token'])

