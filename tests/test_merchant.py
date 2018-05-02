import unittest

from tests.test_helper import TestHelper


class TestMerchant(unittest.TestCase):
    def setUp(self):
        self.client = TestHelper.get_test_client()

    def test_get_merchant_details(self):
        merchant_details = self.client.merchant.get_details(merchant_id=TestHelper.MERCHANT_ID)
        import ipdb; ipdb.set_trace()
