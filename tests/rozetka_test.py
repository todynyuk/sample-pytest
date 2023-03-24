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
    assert  True
    logger.info("'test_test' test was successfully finished")






def attach_screenshot(driver):
    driver.save_screenshot("screenshot.png")
    attach_test_screenshot("screenshot.png")