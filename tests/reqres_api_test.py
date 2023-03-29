import logging
import time

import requests
from pytest_zebrunner import attach_test_run_label, attach_test_run_artifact_reference, attach_test_label
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
from pytest_zebrunner import CurrentTestRun

from api_requests.api_requests import ReqresInApi
from api_validations.api_validations import Validations
from utils.attachments import attach_screenshot

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)

attach_test_run_label("TestRunLabelRunName", "PyTest")
attach_test_run_label("TestRunLabelResourceName", "ReqresAPI")

attach_test_run_artifact_reference("ReqresAPI", "https://reqres.in/")

CurrentTestRun.set_locale("en_US")
CurrentTestRun.set_build("TR build version")


def test_request_response(driver):
    response = requests.get('https://solvdinternal.zebrunner.com')
    assert response.ok, "Response not as expected."
