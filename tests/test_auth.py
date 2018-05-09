import responses
import trekkpay

from tests.utils import SDKTestCase


class TestAuth(SDKTestCase):
    @responses.activate
    def test_auth_fail(self):
        self.prepare_mock_data(responses, mock_data='authFailed')
        client = trekkpay.Client(config=trekkpay.Config(public_key=self.SECRET_KEY, secret_key=self.PUBLIC_KEY))
        result = client.merchant.get_details(merchant_id=self.MERCHANT_ID)
        self.assertFalse(result.is_success)
        self.assertEqual(result.error.code, trekkpay.errors.CODE_AUTH_FAILED)
        self.assertEqual(result.error.message, trekkpay.errors.MSG_AUTH_FAILED)
        self.assertNotEqual(result.auth_key, self.AUTH_KEY)

    @responses.activate
    def test_auth_success(self):
        self.prepare_mock_data(responses, mock_data='v1.merchant.getDetails')
        result = self.client.merchant.get_details(merchant_id=self.MERCHANT_ID)
        self.assertTrue(result.is_success)
        self.assertFalse(hasattr(result, 'error'))
        self.assertEqual(self.config.public_key, self.PUBLIC_KEY)
        self.assertEqual(self.config.secret_key, self.SECRET_KEY)
        self.assertEqual(result.auth_key, self.AUTH_KEY)
