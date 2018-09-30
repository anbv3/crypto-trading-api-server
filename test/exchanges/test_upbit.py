import json
import logging.config
import os
from unittest import TestCase

from app.exchanges.upbit import Upbit

base_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(base_dir, '../logging.json'), 'rt') as f:
    config = json.load(f)
logging.config.dictConfig(config)


class TestUpbit(TestCase):
    def test_get_all_market_codes(self):
        up_bit = Upbit()
        resp = up_bit.get_all_market_codes()
        logging.debug(resp)
