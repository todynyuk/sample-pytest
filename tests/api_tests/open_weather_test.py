import pytest
from api_methods.open_weather_methods import get_open_weather_info_by_city_name, \
    get_open_weather_info_by_city_name_and_country_code, get_open_weather_info_by_city_id, \
    get_open_weather_info_by_coordinates

API_KEY = "01c435c470d484dd56a0b48fd2a06df2"

parameters = [("New York"), ("Vancouver"), ("Buenos Aires")]


@pytest.mark.maintainer("todynyuk")
@pytest.mark.parametrize("city_name", parameters)
def test_open_weather_by_city_name(city_name):
    data = get_open_weather_info_by_city_name(city_name, API_KEY)
    city_data = data["name"]
    assert city_data == city_name


parameters = [("New York", "US"), ("Vancouver", "CA"), ("Buenos Aires", "AR")]


@pytest.mark.maintainer("todynyuk")
@pytest.mark.parametrize("city,country", parameters)
def test_open_weather_by_city_and_country_code(city, country):
    data = get_open_weather_info_by_city_name_and_country_code(city, country, API_KEY)
    country_data = data["sys"]["country"]
    city_data = data["name"]
    assert city == city_data
    assert country_data == country


parameters = [("5128638", "New York"), ("5814616", "Vancouver"), ("6559994", "Buenos Aires")]


@pytest.mark.maintainer("todynyuk")
@pytest.mark.parametrize("city_id,city_name", parameters)
def test_open_weather_by_city_id(city_id, city_name):
    data = get_open_weather_info_by_city_id(city_id, API_KEY)
    city_data = data["name"]
    city_id_data = data["id"]
    assert city_id == str(city_id_data)
    assert city_data == city_name


parameters = [("43.000351", "-75.4999", "New York"), ("45.638729", "-122.661491", "Vancouver"),
              ("-9.12417", "-78.497498", "Buenos Aires")]


@pytest.mark.maintainer("todynyuk")
@pytest.mark.parametrize("lat,lon,city_name", parameters)
def test_open_weather_by_coordinates(lat, lon, city_name):
    data = get_open_weather_info_by_coordinates(lat, lon, API_KEY)
    city_data = data["name"]
    assert city_data == city_name
