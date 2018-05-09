import responses
import trekkpay

from tests.utils import SDKTestCase


class TestMerchant(SDKTestCase):
    @responses.activate
    def test_get_merchant_details(self):
        self.prepare_mock_data(responses, mock_data='v1.merchant.getDetails')
        result = self.client.merchant.get_details(merchant_id=self.MERCHANT_ID)
        self.assertTrue(result.is_success)

