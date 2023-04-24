import logging

import pytest

from utils.bookings import Bookings

from utils.http_manager import HttpManager

import logging
from pytest_zebrunner import attach_test_run_label, attach_test_run_artifact_reference
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
from pytest_zebrunner import CurrentTestRun
from utils.attachments import attach_screenshot

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)

attach_test_run_label("TestRunLabelRunName", "PyTest")
attach_test_run_label("TestRunLabelResourceName", "BookingAPI")

attach_test_run_artifact_reference("BookingAPI", "https://restful-booker.herokuapp.com")

CurrentTestRun.set_locale("en_US")
CurrentTestRun.set_build("TR build version")


class Test_Booking_API_GetTests:

    @pytest.mark.maintainer("todynyuk")
    def test_get_booking(self, driver):
        response = HttpManager.get(Bookings.GET_BOOKING.format(Bookings.get_random_booking()))
        attach_screenshot(driver)
        assert response.status_code == 200, \
            f"Error: status code is not correct. Expected: 200, Actual: {response.status_code}"
        assert isinstance(response.json()['firstname'], str), "Isinstance is not str"
        assert isinstance(response.json()['depositpaid'], bool), "Isinstance is not bool"
        logger.info("'test_get_booking' was successfully finished")

    @pytest.mark.maintainer("todynyuk")
    def test_get_booking_ids(self, driver):
        response = HttpManager.get(Bookings.GET_BOOKINGS)
        attach_screenshot(driver)
        assert response.status_code == 200, \
            f"Error: status code is not correct. Expected: 200, Actual: {response.status_code}"
        assert isinstance(response.json()[0]['bookingid'], int), "Isinstance is not int"
        logger.info("'test_get_booking_ids' was successfully finished")
