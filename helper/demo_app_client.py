from json import dumps
from config import BASE_URI
from config import USER_NAME
from config import PWD
from helper.api_request_helper import Request
from requests.auth import HTTPBasicAuth


class DemoAppClient():

    def __init__(self):
        self.base_url = BASE_URI
        self.user_name = USER_NAME
        self.password = PWD
        self.request = Request()

    def get_auth_token(self):
        auth = HTTPBasicAuth(self.user_name, self.password)
        response = self.request.get_token(self.base_url + '/api/auth/token', auth)
        return response.as_dict["token"]

    def get_registered_users(self, token):
        headers = {'Authorization': token, 'Content-Type': 'application/json'}
        return self.request.get(self.base_url + '/api/users', headers)

    def get_single_user(self, token, username):
        endpoint = "/api/users/" + username
        headers = {'Authorization': token, 'Content-Type': 'application/json'}
        return self.request.get(self.base_url + endpoint, headers)

    def update_user(self, token, username):
        endpoint = "/api/users/" + username
        headers = {'Authorization': token, 'Content-Type': 'application/json'}
        payload = dumps({
            'datapoint1': username
        })
        return self.request.put(self.base_url + endpoint, payload, headers)