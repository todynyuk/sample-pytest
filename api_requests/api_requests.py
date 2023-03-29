import requests
import json

from utils.json_utils import write_response_to_file

BASE_URL = "https://reqres.in/"
FILE_PATH = "/Users/tarasodynyuk/PycharmProjects/web_tests/resources/api/"


def get_list_users():
    endpoint = "api/users?page=2"
    get_url = BASE_URL + endpoint
    json_rs_path = f"{FILE_PATH}get/rs.json"
    response = requests.get(get_url)
    response_json = json.loads(response.text)
    write_response_to_file(json_rs_path, response_json)
    return response
