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


class TestSuitPositive:
    @pytest.mark.maintainer("todynyuk")
    def test_get_list_users(self, driver):
        response = ReqresInApi.get_list_users()
        attach_screenshot(driver)
        request_method = response.request.method
        assert request_method == 'GET'
        assert Validations.valid_status_code(response, 200), "Status code not as expected."
        assert Validations.response_time(response, 600), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {600} ms."
        logger.info("Successful GET request(list_users)")

    parameters = [(2), (3)]

    @pytest.mark.maintainer("todynyuk")
    @pytest.mark.parametrize("user_id", parameters)
    def test_get_single_user(self, driver, user_id):
        response = ReqresInApi.get_single_user(user_id)
        attach_screenshot(driver)
        request_method = response.request.method
        assert request_method == 'GET'
        assert Validations.valid_status_code(response, 200), \
            f"Error: status code is not correct. Expected: 200, Actual: {response.status_code}"
        assert Validations.response_time(response, 600), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {600} ms."
        logger.info("Successful GET request(single_user)")

    parameters = [("Matthew", "programmer"), ("Steve", "designer"), ("Josh", "QA engineer")]

    @pytest.mark.maintainer("todynyuk")
    @pytest.mark.parametrize("name,job", parameters)
    def test_create_new_user(self, driver, name, job):
        response = ReqresInApi.create_new_user(name, job)
        attach_screenshot(driver)
        request_method = response.request.method
        assert request_method == 'POST'
        assert Validations.valid_status_code(response, 201), \
            f"Error: status code is not correct. Expected: 201, Actual: {response.status_code}"
        assert Validations.check_json_keys(response, ["name", "job", "id", "createdAt"]), \
            "The expected set of keys does not match the actual one."
        assert Validations.response_time(response, 800), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {800} ms."
        logger.info("Successful POST request(create_new_user)")

    parameters = [("Steven", "developer", 2), ("Robert", "game designer", 3),
                  ("Mike", "Project Manager", 5)]

    @pytest.mark.maintainer("todynyuk")
    @pytest.mark.parametrize("name,job,user_id", parameters)
    def test_update_user(self, driver, name, job, user_id):
        response = ReqresInApi.update_user(name, job, user_id)
        attach_screenshot(driver)
        request_method = response.request.method
        assert request_method == 'PUT'
        assert Validations.valid_status_code(response, 200), \
            f"Error: status code is not correct. Expected: 200, Actual: {response.status_code}"
        assert Validations.check_json_keys(response, ["name", "job", "updatedAt"]), \
            "The expected set of keys does not match the actual one."
        assert Validations.response_time(response, 800), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {800} ms."
        logger.info("Successful PUT request(update_user)")

    parameters = [(2), (3)]

    @pytest.mark.maintainer("todynyuk")
    @pytest.mark.parametrize("user_id", parameters)
    def test_delete_user(self, driver, user_id):
        response = ReqresInApi.delete_user(user_id)
        attach_screenshot(driver)
        request_method = response.request.method
        assert request_method == 'DELETE'
        assert Validations.valid_status_code(response, 204), \
            f"Error: status code is not correct. Expected: 204, Actual: {response.status_code}"
        assert Validations.response_time(response, 800), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {800} ms."
        logger.info("Successful DELETE request")

    parameters = [("janet.weaver@reqres.in", "ReqRes"), ("emma.wong@reqres.in", "Curly")]

    @pytest.mark.maintainer("todynyuk")
    @pytest.mark.parametrize("username,password", parameters)
    def test_registration_user(self, driver, username, password):
        response = ReqresInApi.register(username, password)
        attach_screenshot(driver)
        request_method = response.request.method
        assert request_method == 'POST'
        assert Validations.valid_status_code(response, 200), \
            f"Error: status code is not correct. Expected: 200, Actual: {response.status_code}"
        assert Validations.check_json_keys(response, ["id", "token"]), \
            "The expected set of keys does not match the actual one."
        assert Validations.response_time(response, 1000), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {1000} ms."
        logger.info("Successful POST request(registration_user)")

    parameters = [("janet.weaver@reqres.in", "ReqRes"), ("emma.wong@reqres.in", "Curly")]

    @pytest.mark.maintainer("todynyuk")
    @pytest.mark.parametrize("username,password", parameters)
    def test_login_user(self, driver, username, password):
        response = ReqresInApi.login(username, password)
        attach_screenshot(driver)
        request_method = response.request.method
        assert request_method == 'POST'
        assert Validations.valid_status_code(response, 200), \
            f"Error: status code is not correct. Expected: 200, Actual: {response.status_code}"
        assert Validations.check_json_keys(response, ["token"]), \
            "The expected set of keys does not match the actual one."
        assert Validations.response_time(response, 1000), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {1000} ms."
        logger.info("Successful POST request(login_user)")

    parameters = [(2), (3)]

    @pytest.mark.maintainer("todynyuk")
    @pytest.mark.parametrize("user_id", parameters)
    def test_get_user_avatar(self, driver, user_id):
        response = ReqresInApi.get_single_user(user_id)
        attach_screenshot(driver)
        request_method = response.request.method
        assert request_method == 'GET'
        assert response.json()['data']['avatar'] == f'https://reqres.in/img/faces/{user_id}-image.jpg', \
            'Avatar is not ok'

    @pytest.mark.maintainer("todynyuk")
    def test_list_resource(self, driver):
        response = ReqresInApi.get_list_resource()
        attach_screenshot(driver)
        request_method = response.request.method
        assert request_method == 'GET'
        assert response.status_code == 200
        response_body = response.json()
        assert response_body['page'] == 1
        assert response_body["per_page"] == 6
        assert response_body["total"] == 12

    parameters = [(2, "fuchsia rose"), (4, "aqua sky"), (5, "tigerlily")]

    @pytest.mark.maintainer("todynyuk")
    @pytest.mark.parametrize("resource_id,name", parameters)
    def test_get_single_resource(self, driver, resource_id, name):
        response = ReqresInApi.get_resource(resource_id)
        attach_screenshot(driver)
        request_method = response.request.method
        assert request_method == 'GET'
        assert response.status_code == 200
        response_body = response.json()
        assert response_body['data']['name'] == name
