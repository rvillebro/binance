import requests
import logging

from typing import TYPE_CHECKING

from binance.enums import http
from binance.client.base import BaseClient
from binance.client.response import Response

if TYPE_CHECKING:
    from binance.client.endpoints.base import _Parameters

log = logging.getLogger(__name__)


class Client(BaseClient):
    """Binance client"""
    ASYNCHRONOUS = False

    def __init__(self, *args, **kwargs):
        self.session = requests.Session()
        super().__init__(*args, *kwargs)

    def __enter__(self) -> None:
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    def close(self) -> None:
        if self.session is not None:
            self.session.close()

    #close.__doc__ = super().close.__doc__

    def _call(self,
              http_method: http.Method,
              route: str,
              /,
              params: '_Parameters' = None,
              headers: dict[str, str] = None,
              add_api_key: bool = False,
              add_signature: bool = False) -> Response:
        if add_api_key is True:
            headers = self._add_api_key(headers)

        if add_signature is True:
            params = self._add_signature(params)

        log.debug("%s call at %s", self.api_url + route, http_method.value)
        req = requests.Request(method=http_method.value,
                               url=self.api_url + route,
                               params=params.urlencode(),
                               headers=headers)

        req = self.session.prepare_request(req)
        response = self.session.send(req)

        return Response.from_requests_response(response)

    #__call.__doc__ = super().__call.__doc__