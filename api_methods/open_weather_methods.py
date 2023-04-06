import requests
import json

from utils.json_utils import write_response_to_file

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
json_rs_path = "/Users/tarasodynyuk/Documents/pytest_demo/python-agent-samples/sample-pytest/resources/api/get/rs.json"

def get_open_weather_info_by_city_name(city, api_key):
    url = BASE_URL + f"q={city}" + f"&appid={api_key}&units=metric"
    response = requests.get(url)
    response_json = json.loads(response.text)
    write_response_to_file(json_rs_path, response_json)
    data = response.json()
    return data

def get_open_weather_info_by_city_id(city_id, api_key):
    url = BASE_URL + f"id={city_id}" + f"&appid={api_key}&units=metric"
    response = requests.get(url)
    response_json = json.loads(response.text)
    write_response_to_file(json_rs_path, response_json)
    data = response.json()
    return data

def get_open_weather_info_by_city_name_and_country_code(city, country_code, api_key):
    url = BASE_URL + f"q={city},{country_code}" + f"&appid={api_key}&units=metric"
    response = requests.get(url)
    response_json = json.loads(response.text)
    write_response_to_file(json_rs_path, response_json)
    data = response.json()
    return data

def get_open_weather_info_by_coordinates(lat, lon, api_key):
    url = BASE_URL + f"lat={lat}&lon={lon}" + f"&appid={api_key}&units=metric"
    response = requests.get(url)
    response_json = json.loads(response.text)
    write_response_to_file(json_rs_path, response_json)
    data = response.json()
    return data
