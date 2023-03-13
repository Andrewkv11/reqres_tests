import requests
from environment import ENV_URL


class CustomRequest:

    @staticmethod
    def get(url, params=None, headers=None, cookies=None):
        return requests.get(
            CustomRequest.full_url(url),
            params=params,
            headers=headers,
            cookies=cookies
        )

    @staticmethod
    def post(url, data=None, headers=None, cookies=None):
        return requests.post(
            CustomRequest.full_url(url),
            data=data,
            headers=headers,
            cookies=cookies,
        )

    @staticmethod
    def put(url, data=None, headers=None, cookies=None):
        return requests.put(
            CustomRequest.full_url(url),
            data=data,
            headers=headers,
            cookies=cookies,
        )

    @staticmethod
    def patch(url, data=None, headers=None, cookies=None):
        return requests.patch(
            CustomRequest.full_url(url),
            data=data,
            headers=headers,
            cookies=cookies,
        )

    @staticmethod
    def delete(url, data=None, headers=None, cookies=None):
        return requests.delete(
            CustomRequest.full_url(url),
            data=data,
            headers=headers,
            cookies=cookies,
        )

    @staticmethod
    def full_url(url):
        return f"{ENV_URL}{url}"
