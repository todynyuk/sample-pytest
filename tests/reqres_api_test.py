import logging
import time

from pytest_zebrunner import attach_test_run_label, attach_test_run_artifact_reference, attach_test_label
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
from pytest_zebrunner import CurrentTestRun

from api_requests.api_requests import ReqresInApi
from api_validations.api_validations import Validations

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)

attach_test_run_label("TestRunLabelRunName", "PyTest")
attach_test_run_label("TestRunLabelResourceName", "ReqresAPI")

attach_test_run_artifact_reference("ReqresAPI", "https://reqres.in/")

CurrentTestRun.set_locale("en_US")
CurrentTestRun.set_build("TR build version")


def test_get_list_users(driver):
    logger.info("Attaching labels, artifacts and artifacts references to test")
    attach_test_label("TestLabel", "ReqresAPI")
    attach_test_run_artifact_reference("ReqresAPI", "https://reqres.in/")
    logger.info("Navigating to url: " + "https://reqres.in/api/users?page=2")
    response = ReqresInApi.get_list_users(driver)
    request_method = response.request.method
    assert request_method == 'GET'
    assert Validations.valid_status_code(response, 200), "Status code not as expected."
    assert Validations.response_time(response, 600), \
        f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {600} ms."
    logger.info("Successful GET request(list_users)")
