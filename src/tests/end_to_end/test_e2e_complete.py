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
    def test_update_booking_with_id_token(self, create_token, get_booking_id):
        print(create_token, get_booking_id)
        booking_id = get_booking_id
        token = create_token
        put_url = ApiConstants.url_patch_put_delete(booking_id=booking_id)
        print(put_url)

        response = post_request(
            url=put_url,
            headers=Utils().common_header_put_delete_patch_cookie(token=token),
            payload=payload_update_booking(),
            auth=None,
            in_json=False
        )
        # Verification here & more
        verify_http_status_code(response_data=response, expected_data=200)

        verify_response_key(response.json()["firstname"], "Amit")
        verify_response_key(response.json()["lastname"], "Brown")


    @allure.title("Test CRUD operation--> DELETE")
    @allure.description("Verify Bookins get deleted with the bookingID and Token")
    @allure.testcase(url="https:qtest.com/tc008655")
    def test_delete_booking_with_id_token(self,create_token,get_booking_id):
        print(create_token,get_booking_id)
        booking_id = get_booking_id
        token = create_token
        delete_url = ApiConstants().url_patch_put_delete(booking_id=booking_id)
        print(delete_url)

        response= delete_request(
            url=delete_url,
            headers=Utils().common_header_put_delete_patch_cookie(token=token),
            auth=None,
            in_json=False
        )
        verify_http_status_code(response_data=response, expected_data=201)



