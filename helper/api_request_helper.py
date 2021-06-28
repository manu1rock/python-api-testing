from dataclasses import dataclass
import requests

@dataclass
class Response:
    status_code: int
    text: str
    as_dict: object
    headers: dict


class Request:
    def get_token(self, endpoint, TokenAuth):
        response = requests.get(endpoint, auth=TokenAuth)
        return self.__get_responses(response)

    def get(self, endpoint, headers):
        response = requests.get(endpoint, headers=headers)
        return self.__get_responses(response)

    def post(self, endpoint, payload, headers):
        response = requests.post(endpoint, data=payload, headers=headers)
        return self.__get_responses(response)

    def put(self, endpoint, payload, headers):
        response = requests.put(endpoint, data=payload, headers=headers)
        return self.__get_responses(response)

    def delete(self, endpoint):
        response = requests.delete(endpoint)
        return self.__get_responses(response)

    def __get_responses(self, response):
        status_code = response.status_code
        text = response.text

        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}

        headers = response.headers

        return Response(
            status_code, text, as_dict, headers
        )
