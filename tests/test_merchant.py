import responses
import trekkpay

from tests.utils import SDKTestCase


class TestMerchant(SDKTestCase):
    @responses.activate
    def test_get_merchant_details_auth_failed(self):
        mock_data = {
            'error': {
                'code': 0,
                'message': 'Authentication failed: Invalid API key.'
            }
        }
        self.prepare_mock_data(responses, mock_data=mock_data)

        result = self.client.merchant.get_details(merchant_id=self.MERCHANT_ID)
        self.assertFalse(result.is_success)
        self.assertEqual(result.error.code, trekkpay.errors.CODE_AUTH_FAILED)
        self.assertEqual(result.error.message, trekkpay.errors.MSG_AUTH_FAILED)

    @responses.is_active
    def test_get_merchant_details_auth_success(self):
        # TODO:
        pass
