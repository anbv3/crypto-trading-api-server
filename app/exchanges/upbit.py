import logging

import requests


class Upbit:
    # https://docs.upbit.com/v1.0/reference
    def __init__(self):
        self.session = requests.Session()

    def __del__(self):
        self.session.close()

    def get_all_market_codes(self):
        url = "https://api.upbit.com/v1/market/all"
        try:
            resp = self.session.get(url)
            logging.debug(resp.status_code)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.HTTPError as e:
            logging.error(str(e))
