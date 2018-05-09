import os
import unittest
import json
import responses

import trekkpay


class SDKTestCase(unittest.TestCase):
    PUBLIC_KEY = 'api_e702422d73e2efff455021180ba0'
    SECRET_KEY = 'sec_fff455021180ba0e702422d73e2e'
    AUTH_KEY = ('YXBpX2U3MDI0MjJkNzNlMmVmZmY0NTUwMjExODBiYTA6ZDcyYTllODIzYjYzMTNjOD'
                'k2MjhlY2QxNWMxY2RiZGI1ZjFiMDdlNjM3MGEyOGQzYTQ1YWNlODY5NWY4YzNhMA==')
    MERCHANT_ID = 101001

    def setUp(self):
        self.config = trekkpay.Config(public_key=self.PUBLIC_KEY, secret_key=self.SECRET_KEY)
        self.client = trekkpay.Client(config=self.config)
        self.responses = responses

    def prepare_mock_data(self, r, mock_data):
        file_path = os.path.join(os.path.dirname(__file__), 'data', '{}.json'.format(mock_data.replace('.', os.sep)))
        with open(file_path, 'r') as json_file:
            mock_data = json.loads(json_file.read())
        r.add(responses.POST, self.config.get_api_url(), json=mock_data, status=200)
