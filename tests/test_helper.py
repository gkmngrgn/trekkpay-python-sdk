import trekkpay


class TestHelper(object):
    PUBLIC_KEY = 'api_e702422d73e2efff455021180ba0'
    SECRET_KEY = 'sec_fff455021180ba0e702422d73e2e'
    MERCHANT_ID = 100001

    @classmethod
    def get_test_config(cls):
        return trekkpay.Config(public_key=cls.PUBLIC_KEY, secret_key=cls.SECRET_KEY)

    @classmethod
    def get_test_client(cls):
        return trekkpay.Client(config=TestHelper.get_test_config())
