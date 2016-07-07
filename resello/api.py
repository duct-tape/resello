import requests
from .managers.vps import VPSManager
from .managers.domain import DomainManager
from .managers.reseller import ResellerManager
from .exceptions import ReselloException
from .models import ReselloResponse


class ReselloClient(object):

    BASE_PATH = 'https://rp01.hostcontrol.com/api/v1'

    def __init__(self, api_key, reseller_reference):

        self.api_key = api_key
        self.reseller_reference = reseller_reference

        self._session = requests.Session()

        if self.api_key and self.reseller_reference:
            self._session.auth = (self.reseller_reference, self.api_key)

        self.reseller = ResellerManager(self)
        self.domain = DomainManager(self)
        self.vps = VPSManager(self)

    def __get_path(self, app_prefix, path):
        return ''.join([self.BASE_PATH, app_prefix, path])

    def handle_error(self, error_response):
        raise ReselloException(
            code=error_response['error']['code'],
            message=error_response['error']['message']
        )

    def handle_request(self, method_name, app_prefix, path, payload=None):
        """
        Makes call via session.method_name.
        Returns result wrapped with :class:ReselloResponse
        """
        path = self.__get_path(app_prefix, path)
        method = getattr(self._session, method_name)
        return ReselloResponse(method(path, json=payload))

    def get(self, app_prefix, path):
        """
        Perform GET request to resello API.
        """
        return self.handle_request('get', app_prefix, path)

    def post(self, app_prefix, path, payload):
        """
        Perform POST request to resello API.
        """
        return self.handle_request('post', app_prefix, path, payload=payload)

    def put(self, app_prefix, path, payload):
        """
        Perform POST request to resello API.
        """
        return self.handle_request('put', app_prefix, path, payload=payload)

    def delete(self, app_prefix, path):
        """
        Perform DELETE request to resello API.
        """
        return self.handle_request('delete', app_prefix, path)
