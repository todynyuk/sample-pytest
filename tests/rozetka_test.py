import logging

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


def test_rozetka(driver):
    logger.info("Attaching labels, artifacts and artifacts references to test")
    attach_test_label("TestLabel", "Rozetka")
    attach_test_run_artifact_reference("Rozetka", "https://rozetka.com.ua/ua/")
    logger.info("Navigating to url: " + url)
    driver.get(url=url)
    attach_screenshot(driver)
    logger.info("Performing search with value: " + search_value)
    search_field: WebElement = driver.find_element(by=By.XPATH, value="//input[contains(@class, 'search-form__input')]")
    search_field.send_keys(search_value)
    search_button: WebElement = driver.find_element(by=By.XPATH,
                                                    value="//button[contains(@class, 'search-form__submit')]")
    search_button.click()
    # search_field.send_keys(Keys.ENTER)
    attach_screenshot(driver)
    logger.info("Verify first search result contains: '" + search_value + "'")
    first_link: WebElement = driver.find_element(by=By.XPATH, value="//span[@class='goods-tile__title'][1]")
    logger.info(first_link.text)
    assert first_link.text.lower().find(search_value.lower()) != -1
    logger.info("'test_rozetka' test was successfully finished")




def attach_screenshot(driver):
    driver.save_screenshot("screenshot.png")
    attach_test_screenshot("screenshot.png")