import logging

import pytest

from api_requests.api_books_requests import get_books, get_book
from pytest_zebrunner import attach_test_run_label, attach_test_run_artifact_reference
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
from pytest_zebrunner import CurrentTestRun
from utils.attachments import attach_screenshot

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)

attach_test_run_label("TestRunLabelRunName", "PyTest")
attach_test_run_label("TestRunLabelResourceName", "BooksAPI")

attach_test_run_artifact_reference("BooksAPI", "https://simple-books-api.glitch.me/books")

CurrentTestRun.set_locale("en_US")
CurrentTestRun.set_build("TR build version")


class TestBooks:

    @pytest.mark.maintainer("todynyuk")
    def test_get_books_200(self, driver):
        response = get_books()
        attach_screenshot(driver)
        assert response.status_code == 200, 'Status code is not ok'
        logger.info("'test_get_books_200' was successfully finished")

    @pytest.mark.maintainer("todynyuk")
    def test_get_books_invalid_type(self, driver):
        response = get_books(book_type='a1b2c0')
        attach_screenshot(driver)
        assert response.status_code == 400, f'Actual status code is incorrect.' \
                                            f' Expected: 400, Actual: {self.response.status_code}'
        assert response.json()['error'] == "Invalid value for query parameter 'type'." \
                                           " Must be one of: fiction, non-fiction.", 'Response message is not correct'
        logger.info("'test_get_books_invalid_type' was successfully finished")

    @pytest.mark.maintainer("todynyuk")
    def test_get_books_limit_greater_than_20(self, driver):
        response = get_books(limit=21)
        attach_screenshot(driver)
        assert response.status_code == 400, f'Actual status code is incorrect.' \
                                            f' Expected: 400, Actual: {self.response.status_code}'
        assert response.json()['error'] == "Invalid value for query parameter 'limit'." \
                                           " Cannot be greater than 20.", 'Response message is not correct'
        logger.info("'test_get_books_limit_greater_than_20' was successfully finished")

    @pytest.mark.maintainer("todynyuk")
    def test_get_books_when_negative_limit(self, driver):
        response = get_books(limit=-5)
        attach_screenshot(driver)
        assert response.status_code == 400, f'Actual status code is incorrect.' \
                                            f' Expected: 400, Actual: {self.response.status_code}'
        assert response.json()['error'] == "Invalid value for query parameter 'limit'." \
                                           " Must be greater than 0.", 'Response message is not correct'
        logger.info("'test_get_books_when_negative_limit' was successfully finished")

    @pytest.mark.maintainer("todynyuk")
    def test_get_books_when_limit_is_0(self, driver):
        response = get_books(limit=0)
        attach_screenshot(driver)
        assert response.status_code == 200, f'Actual status code is incorrect.' \
                                            f' Expected: 200, Actual: {self.response.status_code}'
        assert len(response.json()) == 6, 'Total books returned is incorrect'
        logger.info("'test_get_books_when_limit_is_0' was successfully finished")

    @pytest.mark.maintainer("todynyuk")
    def test_get_all_books(self, driver):
        response = get_books(limit=6)
        attach_screenshot(driver)
        assert len(response.json()) == 6, 'Total books returned is incorrect'
        logger.info("'test_get_all_books' was successfully finished")

    @pytest.mark.maintainer("todynyuk")
    def test_verify_books_attributes(self, driver):
        response = get_books()
        attach_screenshot(driver)
        rez = response.json()
        result = list(rez[0].keys())

        for item in list((response.json()[0]).keys()):
            assert item in result == ['id', 'name', 'type', 'available'], "Attribute doesn't exist"
        logger.info("'test_verify_books_attributes' was successfully finished")

    @pytest.mark.maintainer("todynyuk")
    def test_get_book(self, driver):
        response = get_book(3)
        attach_screenshot(driver)
        expected = {"id": 3,
                    "name": "The Vanishing Half",
                    "author": "Brit Bennett",
                    "type": "fiction",
                    "price": 16.2,
                    "current-stock": 987,
                    "available": True}
        assert response.status_code == 200, f'Actual status code is incorrect.' \
                                            f' Expected: 200, Actual: {self.response.status_code}'
        assert response.json() == expected, 'Response body is incorrect'
        logger.info("'test_get_book' was successfully finished")

    @pytest.mark.maintainer("todynyuk")
    def test_get_book_invalid_id(self, driver):
        response = get_book(87524)
        attach_screenshot(driver)
        assert response.status_code == 404, f'Actual status code is incorrect.' \
                                            f' Expected: 404, Actual: {self.response.status_code}'
        assert response.json()['error'] == "No book with id 87524", 'Wrong message error was returned'
        logger.info("'test_get_book_invalid_id' was successfully finished")
