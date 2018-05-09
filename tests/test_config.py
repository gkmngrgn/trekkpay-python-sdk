import trekkpay

from tests.utils import SDKTestCase


class TestMerchant(SDKTestCase):
    def test_config_url(self):
        config = trekkpay.Config(public_key=self.PUBLIC_KEY, secret_key=self.SECRET_KEY, sandbox=True)
        self.assertEqual(config.get_api_url(), 'https://api.sandbox.trekkpay.io/v1')

        config = trekkpay.Config(public_key=self.PUBLIC_KEY, secret_key=self.SECRET_KEY, sandbox=False)
        self.assertEqual(config.get_api_url(), 'https://api.trekkpay.io/v1')
