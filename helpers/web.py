from urllib.parse import urljoin

import requests


class Connector(requests.Session):
    def __init__(self, base_url=None):
        super().__init__()
        self.base_url = base_url
        self.verify = True
        self.headers.update({'user-agent': 'pytest-playwright'})

    def request(self, method, url, *args, **kwargs):
        joined_url = urljoin(self.base_url, url)
        return super().request(method, joined_url, *args, **kwargs)