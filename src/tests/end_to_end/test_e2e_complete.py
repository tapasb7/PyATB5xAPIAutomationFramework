import allure
import pytest

from src.constants.api_constants import ApiConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils

class TestE2E(object):

    @allure.title("Test End to End")
    @allure.description("Verify after create booking --> Update --> Delete booking // CRUD operation")
    @allure.testcase(url="https:qtest.com/tc008654")
    def test_update_booking_with_id_token(self,create_token,get_booking_id):
        print(create_token,get_booking_id)
        # booking_id = get_booking_id
        # token = create_token
        # put_url = ApiConstants.url_patch_put_delete(booking_id=booking_id)
        # print(put_url)



    @allure.title("Test CRUD operation--> DELETE")
    @allure.description("Verify Bookins get deleted with the bookingID and Token")
    @allure.testcase(url="https:qtest.com/tc008654")
    def test_delete_booking(self,create_token,get_booking_id):
        print(create_token,get_booking_id)
