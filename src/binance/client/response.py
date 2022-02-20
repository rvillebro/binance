import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aiohttp import ClientResponse as AIOHTTPResponse
    from requests import Response as RequestsResponse


class ResponseException(Exception):

    def __init__(self, status: int, reason: str, data: dict, raw: object):
        self.status = status
        self.reason = reason
        self.data = data
        self.raw = raw

    def __str__(self):
        return f"http_status_code={self.status}, reason={self.reason}, data={self.data}"


class Response:
    """Binance response"""
    REQUEST_WEIGHT = re.compile(r'X-MBX-USED-WEIGHT-.*')
    ORDERS = re.compile(r'X-MBX-ORDER-COUNT-.*')

    def __init__(self, data: dict, status: int, limits: dict,
                 raw: object) -> 'Response':
        self.data = data
        self.status = status
        self.limits = limits
        self.raw = raw

    @staticmethod
    def get_limits(headers):
        limits = dict()
        for key, val in headers.items():
            if key.startswith('X-MBX-USED-WEIGHT-') or key.startswith(
                    'X-MBX-ORDER-COUNT-'):
                limits[key] = val
        return limits

    @classmethod
    async def from_aiohttp_response(cls, response: 'AIOHTTPResponse'):
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
    def from_requests_response(cls, response: 'RequestsResponse'):
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

    def __repr__(self):
        return f"Response(status={self.status}, data={self.data})"
