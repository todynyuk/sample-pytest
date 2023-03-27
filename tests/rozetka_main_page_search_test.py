import logging

from pytest_zebrunner import attach_test_run_label, attach_test_run_artifact_reference, attach_test_label, \
    attach_test_screenshot
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
from pytest_zebrunner import CurrentTestRun
from selenium.webdriver.common.by import By

from pages.main_page import set_search_input, click_search_button, verify_is_search_brand_present_in_goods_title, \
    verify_wrong_search_request

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)

attach_test_run_label("TestRunLabelRunName", "PyTest")
attach_test_run_label("TestRunLabelResourceName", "Rozetka")

attach_test_run_artifact_reference("Rozetka", "https://rozetka.com.ua/ua/")

CurrentTestRun.set_locale("en_US")
CurrentTestRun.set_build("TR build version")

url = "https://rozetka.com.ua/ua/"
search_value = "Samsung"


def test_rozetka_correct_search(driver):
    logger.info("Attaching labels, artifacts and artifacts references to test")
    attach_test_label("TestLabel", "Rozetka")
    attach_test_run_artifact_reference("Rozetka", "https://rozetka.com.ua/ua/")
    logger.info("Navigating to url: " + url)
    driver.get(url=url)
    attach_screenshot(driver)
    logger.info("Performing search with value: " + search_value)
    set_search_input(driver, search_value)
    click_search_button(driver)
    attach_screenshot(driver)
    logger.info("Verify first search result contains: '" + search_value + "'")
    assert verify_is_search_brand_present_in_goods_title(driver,search_value), "Search text not" \
                                                                        " contains in all " \
                                                                        "goods title texts"
    logger.info("'test_rozetka_correct_search' was successfully finished")


def test_rozetka_incorrect_search(driver):
    logger.info("Attaching labels, artifacts and artifacts references to test")
    attach_test_label("TestLabel", "Rozetka")
    attach_test_run_artifact_reference("Rozetka", "https://rozetka.com.ua/ua/")
    logger.info("Navigating to url: " + url)
    driver.get(url=url)
    attach_screenshot(driver)
    logger.info("Performing search with value: " + "hgvhvg")
    set_search_input(driver, "hgvhvg")
    click_search_button(driver)
    attach_screenshot(driver)
    logger.info("Verify not_found_text is present")
    assert verify_wrong_search_request(driver), "Wrong request text isn`t presented"
    logger.info("'test_rozetka_incorrect_search' was successfully finished")


def attach_screenshot(driver):
    driver.save_screenshot("screenshot.png")
    attach_test_screenshot("screenshot.png")
