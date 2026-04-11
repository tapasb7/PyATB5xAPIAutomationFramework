import pytest
import allure
import json
import logging #use to print logs
from src.helpers.api_requests_wrapper import get_request
from src.constants.api_constants import ApiConstants
# from src.helpers.payload_manager import *
from src.helpers.common_verification import *
# from src.utils.utils import Utils

class TestGetAllBookingIds:
    @pytest.mark.positive
    @allure.title('Verify the list of booking ids are available')
    @allure.description('Verify the list of booking ids are available')
    def test_GetAllBookingIds(self):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("Starting of Testcase")
        response = get_request(
            url = ApiConstants().url_get_allbookingIds(),
            auth = None,
            in_json = False)
        LOGGER.info('Post request done')
        LOGGER.info('Now Verify the list of booking ids are available')
        verify_http_status_code(response_data=response, expected_data=200)
        response_data = response.json()
        with open(r'./allbookings.json', 'w', encoding='utf-8') as outfile:
            json.dump(response_data, outfile)



        

