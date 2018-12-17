from trekkpay import exceptions
from trekkpay import utils
from trekkpay.config import Config
from trekkpay.merchant import Merchant


class Client(object):
    def __init__(self, config):
        self.merchant = Merchant(config=config)
