from trekkpay.base import BaseAPI
from trekkpay.exceptions import ParameterError
from trekkpay.models import BankAccount, Contact
from trekkpay.utils import UserRole


class Merchant(BaseAPI):
    def create(self, name, integrator_id, contact, bank_account, **kwargs):
        """
        Create a new merchant.

        :param str name: Merchant name (max_length: 200).
        :param str integrator_id: Integrator this merchant belongs to. Can only be set to integrators your API key is
            authorized to use (max_length: 40).
        :param Contact contact: Merchant contact information.
        :param dict bank_account: A bank account.
        :param kwargs: Optional parameters.
        :returns: trekkpay.base.Result
        """
        if isinstance(integrator_id, int):
            integrator_id = str(integrator_id)

        if not isinstance(contact, Contact):
            raise ParameterError("`contact` parameter should be a Contact object.")

        if not isinstance(bank_account, BankAccount):
            raise ParameterError("`bank_account` parameter should be a BankAccount object.")


        request_data = {
            'method': 'merchant.create',
            'params': {
                'name': name,
                'integrator_id': integrator_id,
                'contact': contact.__dict__,
                'bank_account': bank_account.__dict__
            }
        }
        request_data['params'].update(**kwargs)
        import ipdb; ipdb.set_trace()
        return self.post_request(request_data)

    def create_user(self, merchant_id, display_name, email, password, roles):
        if set(roles).difference(UserRole.get_list()):
            raise ParameterError("All user roles are not valid.")

        request_data = {
            'method': 'merchant.createUser',
            'params': {
                'merchant_id': merchant_id,
                'display_name': display_name,
                'email': email,
                'password': password,
                'roles': roles
            }
        }
        return self.post_request(request_data)

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
