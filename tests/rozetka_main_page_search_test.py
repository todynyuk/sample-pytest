import logging
import time

from pytest_zebrunner import attach_test_run_label, attach_test_run_artifact_reference, attach_test_label, \
    attach_test_screenshot
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
from pytest_zebrunner import CurrentTestRun
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

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


def test_test(driver):
    logger.info("Attaching label to test")
    attach_test_label("Test", "Assert")
    assert True
    logger.info("'test_test' test was successfully finished")


def test_rozetka_correct_search(driver):
    logger.info("Attaching labels, artifacts and artifacts references to test")
    attach_test_label("TestLabel", "Rozetka")
    attach_test_run_artifact_reference("Rozetka", "https://rozetka.com.ua/ua/")
    logger.info("Navigating to url: " + url)
    driver.get(url=url)
    attach_screenshot(driver)
    logger.info("Performing search with value: " + search_value)
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[contains(@class, 'search-form__input')]").send_keys(search_value)
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[contains(@class, 'search-form__submit')]").click()
    attach_screenshot(driver)
    time.sleep(10)
    logger.info("Verify first search result contains: '" + search_value + "'")
    xpath = f"//span[@class='goods-tile__title'][{1}]"
    goods_title_text = driver.find_element(By.XPATH, xpath).text
    logger.info(goods_title_text)
    assert str(goods_title_text.lower()).__contains__(
        search_value.lower()), "Device description not contains search_value"
    logger.info("'test_rozetka_correct_search' test was successfully finished")


def test_rozetka_incorrect_search(driver):
    logger.info("Attaching labels, artifacts and artifacts references to test")
    attach_test_label("TestLabel", "Rozetka")
    attach_test_run_artifact_reference("Rozetka", "https://rozetka.com.ua/ua/")
    logger.info("Navigating to url: " + url)
    driver.get(url=url)
    attach_screenshot(driver)
    logger.info("Performing search with value: " + "hgvhvg")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[contains(@class, 'search-form__input')]").send_keys("hgvhvg")
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[contains(@class, 'search-form__submit')]").click()
    attach_screenshot(driver)
    time.sleep(10)
    logger.info("Verify not_found_text is present")
    assert driver.find_element(By.XPATH, "//span[@class='ng-star-inserted']").is_displayed()
    logger.info("'test_rozetka_incorrect_search' test was successfully finished")


def attach_screenshot(driver):
    driver.save_screenshot("screenshot.png")
    attach_test_screenshot("screenshot.png")
