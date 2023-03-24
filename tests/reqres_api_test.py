import logging
import requests

from pytest_zebrunner import attach_test_run_label, attach_test_run_artifact_reference, attach_test_label, \
    attach_test_screenshot
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
from pytest_zebrunner import CurrentTestRun

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)

attach_test_run_label("TestReqresAPI", "PyTest")

attach_test_run_artifact_reference("ReqresApi", "https://reqres.in/")

CurrentTestRun.set_locale("en_US")
CurrentTestRun.set_build("TR build version")
BASE_URL = "https://reqres.in/"


def test_get_list_users(driver):
    logger.info("Attaching label to test")
    attach_test_label("Test", "ReqresAPI")
    endpoint = "api/users?page=2"
    get_url = BASE_URL + endpoint
    response = requests.get(get_url)
    request_method = response.request.method
    assert request_method == 'GET'
    assert response.status_code == 200, "Status code not as expected."
    assert (response.elapsed.total_seconds() * 1000) < 600, \
        f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {600} ms."
    logger.info("Successful GET request(list_users)")


def attach_screenshot(driver):
    driver.save_screenshot("screenshot.png")
    attach_test_screenshot("screenshot.png")