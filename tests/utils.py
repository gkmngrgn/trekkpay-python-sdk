import unittest
import responses

import trekkpay


class SDKTestCase(unittest.TestCase):
    PUBLIC_KEY = 'api_e702422d73e2efff455021180ba0'
    SECRET_KEY = 'sec_fff455021180ba0e702422d73e2e'
    MERCHANT_ID = 100001

    def setUp(self):
        self.config = trekkpay.Config(public_key=self.PUBLIC_KEY, secret_key=self.SECRET_KEY)
        self.client = trekkpay.Client(config=self.config)
        self.responses = responses

    def prepare_mock_data(self, r, mock_data):
        mock_data.update({
            'jsonrpc': '2.0',
            'id': 1
        })
        r.add(responses.POST, self.config.get_api_url(), json=mock_data, status=200)
