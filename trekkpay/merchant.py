from trekkpay.base import BaseAPI


class Merchant(BaseAPI):
    def create(self):
        # TODO:
        pass

    def get_details(self, merchant_id):
        request_data = {
            'method': 'merchant.getDetails',
            'params': {
                'merchant_id': merchant_id,
            }
        }
        return self.post_request(request_data)

    def remove_bank_account(self):
        # TODO:
        pass

    def set_bank_account(self):
        # TODO:
        pass

    def update(self):
        # TODO:
        pass
