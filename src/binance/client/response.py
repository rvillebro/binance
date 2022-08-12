import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aiohttp import ClientResponse as AIOHTTPResponse
    from requests import Response as RequestsResponse


class ResponseException(Exception):
    """
    Response exception

    Parameters
    ----------
    status: int
        Status of response
    reason: str
        Reason of response
    data: dict
        Data of response 
    raw: object
        Raw sponse object
    """

    def __init__(self, status: int, reason: str, data: dict, raw: object):
        self.status = status
        self.reason = reason
        self.data = data
        self.raw = raw

    def __str__(self):
        return f"http_status_code={self.status}, reason={self.reason}, data={self.data}"


class Response:
    """
    Binance client response

    Parameters
    ----------
    data: dict
        Response data (JSON converted to a dcitionary)
    status: int
        Response status code
    limits: dict
        API limits from response
    raw: object
        Raw response object 
    """
    REQUEST_WEIGHT = re.compile(r'X-MBX-USED-WEIGHT-.*')
    ORDERS = re.compile(r'X-MBX-ORDER-COUNT-.*')

    def __init__(self, data: dict, status: int, limits: dict,
                 raw: object):
        self.data = data
        self.status = status
        self.limits = limits
        self.raw = raw
    
    def __repr__(self) -> str:
        return f"Response(status={self.status}, data={self.data})"

    @staticmethod
    def get_limits(headers) -> dict:
        """
        Gets limits from headers

        Parameters
        ----------
        headers: dict[str, str]
            Headers of response
        
        Returns
        -------
        dict
            Limits of extracted from response
        """
        limits = dict()
        for key, val in headers.items():
            if key.startswith('X-MBX-USED-WEIGHT-') or key.startswith(
                    'X-MBX-ORDER-COUNT-'):
                limits[key] = val
        return limits

    @classmethod
    async def from_aiohttp_response(cls, response: 'AIOHTTPResponse') -> 'Response':
        """
        Creates binance response from aiohttp response object

        Parameters
        ----------
        response: :class:`aiohttp.ClientResponse`
            aiohttp reponse object
        
        Returns
        -------
        :class:`binance.client.response.Response`
            Binance client response
        """
        if not response.ok:
            raise ResponseException(status=response.status,
                                    reason=response.reason,
                                    dict=await response.json(),
                                    raw=response)

        data = await response.json()
        limits = cls.get_limits(response.headers)
        return cls(data=data,
                   status=response.status,
                   limits=limits,
                   raw=response)

    @classmethod
    def from_requests_response(cls, response: 'RequestsResponse') -> 'Response':
        """
        Creates binance response from requests response object

        Parameters
        ----------
        response: :class:`requests.Response`
            requests reponse object
        
        Returns
        -------
        :class:`binance.client.response.Response`
            Binance client response
        """
        if not response.ok:
            raise ResponseException(status=response.status_code,
                                    reason=response.reason,
                                    data=response.json(),
                                    raw=response)

        data = response.json()
        limits = cls.get_limits(response.headers)
        return cls(data=data,
                   status=response.status_code,
                   limits=limits,
                   raw=response)
