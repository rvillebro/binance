import os
import abc
import hmac
import hashlib

from dotenv import load_dotenv
from typing import TYPE_CHECKING

from binance.constants import NETWORK
from binance.client import endpoints

if TYPE_CHECKING:
    from binance.enums import http
    from binance.client.response import Response
    from binance.client.endpoints.base import APIParameters

load_dotenv()


class BaseClient(abc.ABC):
    """
    Client abstract base class

    Parameters
    ----------
    api_key: str
        API access key id
    api_secret: str
        API secret acces key (keep it secret!)
    mode: :class:`binance.constants.NETWORK`
        Network mode, either real or test
    api_url: str
        Binance API base url
    websocket_url: str
        Binance websocket base url
    """
    #: indicates whether endpoints should be asynchronous
    ASYNCHRONOUS: bool

    def __init__(self,
                 api_key: str = os.environ.get('BINANCE_API_KEY'),
                 api_secret: str = os.environ.get('BINANCE_API_SECRET'),
                 mode: NETWORK = NETWORK.TEST,
                 api_url: str = None,
                 websocket_url: str = None):
        if mode:
            self.api_url = mode['API']
            self.websocket_url = mode['WEBSOCKET']

        # overwrite base rest and websocket uri if defined
        if api_url:
            self.api_url = api_url
        if websocket_url:
            self.websocket_url = websocket_url

        self._api_key = api_key
        self._api_secret = api_secret

        self.market = endpoints.Market.link(self)
        self.trade = endpoints.Trade.link(self)
        self.user_data = endpoints.UserData.link(self)

    def _add_api_key(self, headers: dict) -> dict[str, str]:
        """Adds API key to headers"""
        if self._api_key is None:
            raise ValueError('Binance futures API key is missing!')
        headers = dict() if headers is None else headers
        headers.update({'X-MBX-APIKEY': self._api_key})
        return headers

    def _add_signature(self, params: 'APIParameters') -> dict[str, str]:
        """Adds signature to params"""
        if self._api_secret is None:
            raise ValueError('Binance futures API secret is missing!')
        url_encoded_params = params.urlencode()
        signature = hmac.new(self._api_secret.encode(),
                             url_encoded_params.encode(),
                             hashlib.sha256).hexdigest()
        params['signature'] = signature
        return params

    @abc.abstractmethod
    def close(self):
        """
        Closes binance client
        """

    @abc.abstractmethod
    def _call(self,
               http_method: 'http.Method',
               route: str,
               /,
               params=None,
               headers=None,
               add_api_key=False,
               add_signature=False) -> 'Response':
        """
        Makes a binance API call

        Parameters
        ----------
        http_method: http.Method
            HTTP method to use.
        route: str
            Route of endpoint
        params: :class:`binance.client.endpoints.base._Parameters`
            Parameters to encode in url
        headers: dict[str, str]
            Headers to include in API call
        add_api_key: bool
            Boolean indicating whether to add API key
        add_signature: bool
            Boolean indicating whether to add API signature
        
        Returns
        -------
        :class:`binance.client.response.Response`
            Binance client response
        """
