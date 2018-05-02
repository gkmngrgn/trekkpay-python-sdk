class Config(object):
    def __init__(self, public_key, secret_key, sandbox=False):
        self.public_key = public_key
        self.secret_key = secret_key
        self.sandbox = sandbox

    def get_api_url(self):
        return 'https://{}.trekkpay.io/v1'.format('api.sandbox' if self.sandbox is True else 'api')
