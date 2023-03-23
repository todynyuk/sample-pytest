import random

from utils.http_manager import HttpManager


class Bookings:
    BASE_URL = "https://restful-booker.herokuapp.com"
    PING = BASE_URL + "/ping"
    AUTH = BASE_URL + "/auth"
    GET_BOOKINGS = BASE_URL + "/booking/"
    GET_BOOKING = BASE_URL + "/booking/{0}"
    CREATE_BOOKING = BASE_URL + "/booking"
    DELETE_BOOKING = BASE_URL + "/booking/{0}"

    @staticmethod
    def get_random_booking() -> str:
        '''Chooses one booking from the list of currently existing ones'''
        return str(random.choice(Bookings.get_existing_booking_ids()))

    @staticmethod
    def get_existing_booking_ids() -> list:
        '''Provides the list of currently existing booking ids'''
        response = HttpManager.get(Bookings.GET_BOOKINGS)
        return [booking['bookingid'] for booking in response.json()]
