import base64
import hashlib
import hmac
import json

import requests


class BaseAPI(object):
    def __init__(self, config, sandbox=False):
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
            str.encode(self.config.secret_key), msg=str.encode(request_data), digestmod=hashlib.sha256).hexdigest()

        # Step 3: create a key with the signature
        authorization_key = bytes.decode(
            base64.b64encode(str.encode('{}:{}'.format(self.config.public_key, signature))))

        headers = {
            'Accept': 'application/json',
            'Authorization': 'Basic {}'.format(authorization_key),
            'Content-Type': 'application/json',
        }
        return requests.post(self.api_url, json=request_data, headers=headers)
