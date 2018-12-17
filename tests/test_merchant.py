import datetime

import responses

from tests.utils import SDKTestCase
from trekkpay.utils import UserRole


class TestMerchant(SDKTestCase):
    @responses.activate
    def test_create_user(self):
        self.prepare_mock_data(responses, mock_data='v1.merchant.createUser')
        result = self.client.merchant.create_user(
            merchant_id=self.MERCHANT_ID,
            display_name='Gökmen Görgen',
            email='gokmen@localhost',
            password='0123456789',
            roles=[UserRole.INTEGRATOR])
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.is_success)

    @responses.activate
    def test_get_details(self):
        self.prepare_mock_data(responses, mock_data='v1.merchant.getDetails')
        result = self.client.merchant.get_details(merchant_id=self.MERCHANT_ID)
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.is_success)

        # Check datetime conversion
        created_at = datetime.datetime(2018, 3, 22, 10, 35, 37, tzinfo=datetime.timezone.utc)
        self.assertEqual(result.created_at, created_at)
