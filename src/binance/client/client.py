#!/usr/bin/env python3
import json
import requests

from binance.enums import http
from binance.client.base import BaseClient

class Client(BaseClient):
    def __init__(self, *args, **kwargs) -> object:
        super().__init__(*args, *kwargs)
        self.session = requests.Session()
    
    def __enter__(self) -> None:
        return self
    
    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    def close(self) -> None:
        if self.session is not None:
            self.session.close()
        
    def _call(self, http_method: http.Method, route: str, /,
              params=None, headers=None, add_api_key=False,
              add_signature=False) -> None:
        if add_api_key is True:
            if self.__api_key is None:
                raise ValueError('Binance futures API key is missing!')
            headers = {} if headers is None else headers
            headers = self.__add_api_key_to_headers(headers)

        if add_signature is True:
            if self.___api_secret is None:
                raise ValueError('Binance futures API secret is missing!')
            params['signature'] = self.__get_signature(params.urlencode())
        
        response = self.session.Request(
            method=http_method.value(),
            utrl=self._rest_base + route,
            params=params.urlencode(),
            headers=headers
        )

        status_code = response.status
        response_body = response.text()
        if len(response_body) > 0:
            response_body = json.loads(response_body)

            return {
                "status_code": status_code,
                "response": response_body
            }
