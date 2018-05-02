from trekkpay.merchant import Merchant
from trekkpay.config import Config


class Client(object):
    def __init__(self, config):
        self.merchant = Merchant(config=config)
