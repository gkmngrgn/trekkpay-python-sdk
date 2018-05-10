import base64
import collections
import datetime
import hashlib
import hmac
import json

import requests


class Result(object):
    status_code = None
    auth_key = None

    def __init__(self, response):
        self.status_code = response.status_code
        self.auth_key = response.request.headers.get('Authorization').strip('Basic ')
        self.data = json.loads(response.text, object_hook=self.__convert_json_to_object)

    def __getattr__(self, item):
        data = self.data.result if self.is_success else self.data
        return getattr(data, item)

    @property
    def is_success(self):
        return not hasattr(self.data, 'error')

    @staticmethod
    def __convert_json_to_object(item):
        if 'created_at' in item:
            created_at = datetime.datetime.strptime(item['created_at'], '%Y-%m-%dT%H:%M:%S%z')
            item.update({'created_at': created_at})
        return collections.namedtuple('Result', item.keys())(*item.values())


class BaseAPI(object):
    def __init__(self, config):
        self.config = config
        self.api_url = config.get_api_url()

    def post_request(self, request_data):
        # modify request data for json-rpc.
        request_data.update({
            'jsonrpc': '2.0',
            'id': 1,
        })

        # Authorization https://developers.trekkpay.io/auth
        # Step 1: encode request data
        encoded_data = base64.b64encode(str.encode(json.dumps(request_data)))
        encoded_data = bytes.decode(encoded_data).rstrip('=').replace('+', '-').replace('/', '_')

        # Step 2: create a signature with the request data
        signature = hmac.new(
            str.encode(self.config.secret_key), msg=str.encode(encoded_data), digestmod=hashlib.sha256).hexdigest()

        # Step 3: create a key with the signature
        authorization_key = bytes.decode(
            base64.b64encode(str.encode('{}:{}'.format(self.config.public_key, signature))))

        headers = {
            'Accept': 'application/json',
            'Authorization': 'Basic {}'.format(authorization_key),
            'Content-Type': 'application/json',
        }

        response = requests.post(self.api_url, json=request_data, headers=headers)
        result = Result(response=response)
        return result
