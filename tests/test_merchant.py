import datetime
import responses

from tests.utils import SDKTestCase
from trekkpay.utils import PayoutCycle, PayoutType


class TestMerchant(SDKTestCase):
    @responses.activate
    def test_get_merchant_details(self):
        self.prepare_mock_data(responses, mock_data='v1.merchant.getDetails')
        result = self.client.merchant.get_details(merchant_id=self.MERCHANT_ID)
        created_at = datetime.datetime(2018, 3, 22, 10, 35, 37, tzinfo=datetime.timezone.utc)

        self.assertTrue(result.is_success)
        self.assertEqual(result.merchant_id, self.MERCHANT_ID)
        self.assertEqual(result.name, 'alaGeek')
        self.assertEqual(result.integrator_id, 'alageek')
        self.assertEqual(result.trekksoft_id, None)
        self.assertEqual(result.dcc_display_option, 'a')
        self.assertEqual(result.created_at, created_at)
        self.assertEqual(result.is_verified, True)
        self.assertEqual(result.is_insurance_enabled, True)
        self.assertEqual(result.is_3d_secure_required, True)
        self.assertEqual(result.is_dunned, False)
        self.assertEqual(result.address.country, 'DE')
        self.assertEqual(result.contact.name, 'Gökmen Görgen')
        self.assertEqual(result.contact.email, 'gkmngrgn@gmail.com')
        self.assertEqual(result.contact.phone, '+4915212345678')
        self.assertEqual(result.payout_fees, [])
        self.assertEqual(result.payout_minimum_amount, 0)
        self.assertEqual(result.payout_withholding_amount, 0)
        self.assertEqual(result.payout_cycle, PayoutCycle.WEEKLY)
        self.assertEqual(result.payout_type, PayoutType.TRANSACTION_DATE)
