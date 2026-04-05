import allure
import pytest

class TestE2E(object):

    @allure.title("Test End to End")
    @allure.description("Verify after create booking --> Update --> Delete booking // CRUD operation")
    @allure.testcase(url="https:qtest.com/tc008654")
    def test_update_booking_with_id_token(self):
        pass

    @allure.title("Test CRUD operation--> DELETE")
    @allure.description("Verify Bookins get deleted with the bookingID and Token")
    @allure.testcase(url="https:qtest.com/tc008654")
    def test_delete_booking(self):
        pass


