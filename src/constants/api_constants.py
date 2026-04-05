#APIConstants class contains all the endpoints

class ApiConstants(object):

    def __init__(self):
        pass

    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def usrl_create_booking(self):
        return 'https://restful-booker.herokuapp.com/booking'

    def url_create_token(self):
        return 'https://restful-booker.herokuapp.com/auth'

    def url_patch_put_delete(booking_id):
        return 'https://restful-booker.herokuapp.com/booking'+str(booking_id)