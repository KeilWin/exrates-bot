import urllib.request
import json


class NetRequests:
    _daily_rates_url: str

    @property
    def daily_rates_url(self):
        return self._daily_rates_url

    def __init__(self, daily_rates_url):
        self._daily_rates_url = daily_rates_url

    def get_rates(self) -> dict:
        with urllib.request.urlopen(self._daily_rates_url) as response:
            text = json.loads(response.read())
            return text
