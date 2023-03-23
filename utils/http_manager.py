import requests
import json


class HttpManager:
    headers = {'Content-Type': 'application/json'}

    @staticmethod
    def auth(url, user, password):
        data = json.dumps({
            'username': user,
            'password': password
        })
        response = requests.post(url, headers=HttpManager.headers, data=data)
        response_json = json.loads(response.text)
        HttpManager.headers['Cookie'] = 'token=' + response_json['token']
        return response

    @staticmethod
    def get(url):
        response = requests.get(url, headers=HttpManager.headers)
        return response

    @staticmethod
    def post(url, data):
        response = requests.post(url, data=data, headers=HttpManager.headers)
        return response

    @staticmethod
    def put(url, data):
        response = requests.put(url, data=data, headers=HttpManager.headers)
        return response

    @staticmethod
    def patch(url, data):
        response = requests.patch(url, data=data, headers=HttpManager.headers)
        return response

    @staticmethod
    def delete(url):
        response = requests.delete(url, headers=HttpManager.headers)
        return response