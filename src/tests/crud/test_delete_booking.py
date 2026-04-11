import pytest
import allure
import logging #use to print logs


from src.helpers.api_requests_wrapper import *
from src.constants.api_constants import ApiConstants
# from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import *
# from src.utils.utils import Utils

class TestDeleteBooking(object):
    @pytest.mark.positive
    @allure.title('Verify that Delete Booking status')
    @allure.description(
        "Delete Booking status")
    def test_delete_booking_positive(self,get_booking_id):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("Starting of Testcase")
        booking_id = get_booking_id
        print("booking_id", booking_id)
        response = delete_request(
            url=ApiConstants().url_patch_put_delete(booking_id=booking_id),
            auth=None,
            headers=None,
            in_json=False
                    )
        LOGGER.info('POST Req Done')
        LOGGER.info('Now Verify')
        verify_http_status_code(response_data=response, expected_data=201)
        LOGGER.info(response.json())
        LOGGER.info(response.json()['bookingid'])




