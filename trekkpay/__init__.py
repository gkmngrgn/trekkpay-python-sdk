from trekkpay import errors
from trekkpay.config import Config
from trekkpay.merchant import Merchant


class Client(object):
    def __init__(self, config):
        self.merchant = Merchant(config=config)
