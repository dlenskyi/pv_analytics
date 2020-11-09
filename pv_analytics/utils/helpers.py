import unicodedata

import requests
from rest_framework import status


def normalize_caseless(text):
    return unicodedata.normalize("NFD", text.casefold())


def caseless_equal(left_text, right_text):
    if left_text and right_text:
        return normalize_caseless(left_text) == normalize_caseless(right_text)
    return False


class Client:
    """
    This is a client used for communicating with the external APIs.
    """

    def __init__(self, headers):
        self.headers = headers

    def make_request(self, method, url, data=None, json=None, **kwargs):
        if json:
            data = json.dumps(json)
        response = requests.request(
            method=method, url=url, data=data, headers=self.headers, **kwargs,
        )
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print("Oops", errh)
        return response

    def get(self, url, **kwargs):
        response = self.make_request(method='GET', url=url, **kwargs)
        if response and response.status_code == status.HTTP_200_OK:
            return response.json()

    def post(self, url, data):
        response = self.make_request(method='POST', url=url, json=data)
        if response is not None:
            return response

    def put(self, url, data):
        response = self.make_request(method='PUT', url=url, json=data)
        if response is not None:
            return response

    def delete(self, url):
        response = self.make_request(method='DELETE', url=url)
        if response is not None:
            return response
