import logging

import requests
from pytest_zebrunner import attach_test_run_label, attach_test_run_artifact_reference, attach_test_label
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
from pytest_zebrunner import CurrentTestRun

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)

attach_test_run_label("TestRunLabelRunName", "PyTest")
attach_test_run_label("TestRunLabelResourceName", "Zebrunner")

attach_test_run_artifact_reference("Zebrunner", "https://solvdinternal.zebrunner.com")

CurrentTestRun.set_locale("en_US")
CurrentTestRun.set_build("TR build version")

url = "https://solvdinternal.zebrunner.com"


def test_request_response(driver):
    logger.info("Attaching labels, artifacts and artifacts references to test")
    attach_test_label("TestLabel", "Zebrunner")
    attach_test_run_artifact_reference("Zebrunner", "https://solvdinternal.zebrunner.com")
    logger.info("Navigating to url: " + url)
    driver.get(url=url)
    response = requests.get()
    assert response.ok, "Response not as expected."
    logger.info("'test_request_response' was successfully finished")
