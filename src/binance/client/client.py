import requests
import logging

from binance.enums import http
from binance.client.base import BaseClient
from binance.client.response import Response

log = logging.getLogger(__file__)


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

    def _call(self,
              http_method: http.Method,
              route: str,
              /,
              params=None,
              headers=None,
              add_api_key=False,
              add_signature=False) -> Response:
        """
        Returns
        -------
        https://2.python-requests.org/en/master/api/#requests.Response
        """
        if add_api_key is True:
            headers = self._add_api_key(headers)

        if add_signature is True:
            params = self._add_signature(params)

        req = requests.Request(method=http_method.value,
                               url=self._rest_base + route,
                               params=params.urlencode(),
                               headers=headers)

        req = self.session.prepare_request(req)
        response = self.session.send(req)

        return Response.from_requests_response(response)
