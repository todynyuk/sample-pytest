from pytest_zebrunner import attach_test_run_label, attach_test_run_artifact_reference, CurrentTestRun

from api_requests.api_requests import ReqresInApi
from api_validations.api_validations import Validations
import logging
import pytest
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
from utils.attachments import attach_screenshot

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)

attach_test_run_label("TestRunLabelRunName", "PyTest")
attach_test_run_label("TestRunLabelResourceName", "ReqresAPI")

attach_test_run_artifact_reference("ReqresAPI", "https://reqres.in/")

CurrentTestRun.set_locale("en_US")
CurrentTestRun.set_build("TR build version")


class TestSuitNegative:
    parameters = [(25), (35)]

    @pytest.mark.maintainer("todynyuk")
    @pytest.mark.parametrize("user_id", parameters)
    def test_get_invalid_single_user(self, driver, user_id):
        response = ReqresInApi.get_single_user(user_id)
        attach_screenshot(driver)
        request_method = response.request.method
        assert request_method == 'GET'
        assert Validations.valid_status_code(response, 404), \
            f"Error: status code is not correct. Expected: 404, Actual: {response.status_code}"
        assert Validations.response_time(response, 800), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {800} ms."
        logger.info("Single user not found. Empty response.")

    parameters = [("", "ReqRes"), ("", "Curly")]

    @pytest.mark.maintainer("todynyuk")
    @pytest.mark.parametrize("username,password", parameters)
    def test_registration_without_email(self, driver, username, password):
        response = ReqresInApi.register(username, password)
        attach_screenshot(driver)
        request_method = response.request.method
        assert request_method == 'POST'
        assert Validations.valid_status_code(response, 400), \
            f"Error: status code is not correct. Expected: 400, Actual: {response.status_code}"
        assert Validations.check_json_keys(response, ["error"]), \
            "The expected set of keys does not match the actual one."
        assert Validations.check_json_values(response, ["Missing email or username"]), \
            "The expected values do not match the actual one."
        assert Validations.response_time(response, 8000), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {8000} ms."
        logger.info("Error: Missing email or username")

    parameters = [("janet.weaver@reqres.in", ""), ("emma.wong@reqres.in", "")]

    @pytest.mark.maintainer("todynyuk")
    @pytest.mark.parametrize("username,password", parameters)
    def test_registration_without_password(self, driver, username, password):
        response = ReqresInApi.register(username, password)
        attach_screenshot(driver)
        request_method = response.request.method
        assert request_method == 'POST'
        assert Validations.valid_status_code(response, 400), \
            f"Error: status code is not correct. Expected: 400, Actual: {response.status_code}"
        assert Validations.check_json_keys(response, ["error"]), \
            "The expected set of keys does not match the actual one."
        assert Validations.check_json_values(response, ["Missing password"]), \
            "The expected values do not match the actual one."
        assert Validations.response_time(response, 8000), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {8000} ms."
        logger.info("Error: Missing password")

    parameters = [("", "ReqRes"), ("", "Curly")]

    @pytest.mark.maintainer("todynyuk")
    @pytest.mark.parametrize("username,password", parameters)
    def test_login_without_email(self, driver, username, password):
        response = ReqresInApi.login(username, password)
        attach_screenshot(driver)
        request_method = response.request.method
        assert request_method == 'POST'
        assert Validations.valid_status_code(response, 400), \
            f"Error: status code is not correct. Expected: 400, Actual: {response.status_code}"
        assert Validations.check_json_keys(response, ["error"]), \
            "The expected set of keys does not match the actual one."
        assert Validations.check_json_values(response, ["Missing email or username"]), \
            "The expected values do not match the actual one."
        assert Validations.response_time(response, 8000), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {8000} ms."
        logger.info("Error: Missing email or username")

    parameters = [("janet.weaver@reqres.in", ""), ("emma.wong@reqres.in", "")]

    @pytest.mark.maintainer("todynyuk")
    @pytest.mark.parametrize("username,password", parameters)
    def test_login_without_password(self, driver, username, password):
        response = ReqresInApi.login(username, password)
        attach_screenshot(driver)
        request_method = response.request.method
        assert request_method == 'POST'
        assert Validations.valid_status_code(response, 400), \
            f"Error: status code is not correct. Expected: 400, Actual: {response.status_code}"
        assert Validations.check_json_keys(response, ["error"]), \
            "The expected set of keys does not match the actual one."
        assert Validations.check_json_values(response, ["Missing password"]), \
            "The expected values do not match the actual one."
        assert Validations.response_time(response, 8000), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {8000} ms."
        logger.info("Error: Missing password")

    parameters = [("123.weaver@reqres.in", "ReqRes"), ("emma150.wong@reqres.in", "Curly")]

    @pytest.mark.maintainer("todynyuk")
    @pytest.mark.parametrize("username,password", parameters)
    def test_login_with_wrong_email(self, driver, username, password):
        response = ReqresInApi.login(username, password)
        attach_screenshot(driver)
        request_method = response.request.method
        assert request_method == 'POST'
        assert Validations.valid_status_code(response, 400), \
            f"Error: status code is not correct. Expected: 400, Actual: {response.status_code}"
        assert Validations.check_json_keys(response, ["error"]), \
            "The expected set of keys does not match the actual one."
        assert Validations.response_time(response, 8000), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {8000} ms."
        logger.info("Error: Incorrect login or password")
