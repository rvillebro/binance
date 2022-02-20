#!/usr/bin/env python3
import pytest
from typing import TYPE_CHECKING
from pydantic import ValidationError

from binance.client.response import ResponseException

if TYPE_CHECKING:
    from binance.client import Client


def test_get_position_mode(client: 'Client'):
    if client._api_key is None:
        pytest.skip("Requires API key!")

    response = client.trade.get_position_mode(recvWindow=30000)

    assert response.status == 200, response


def test_set_position_mode(client: 'Client'):
    if client._api_key is None and client._api_secret is None:
        pytest.skip("Requires API key and secret!")

    func = client.trade.set_position_mode
    with pytest.raises(ValidationError):
        func()

    client.trade.set_position_mode

    response = client.trade.get_position_mode(recvWindow=30000)
    assert response.status == 200, response

    dualSidePosition = response.data['dualSidePosition']
    with pytest.raises(ResponseException) as e:
        response = func(dualSidePosition=dualSidePosition, recvWindow=30000)
    assert e.value.status == 400, response
    assert e.value.data['code'] == -4059, response

    response = func(dualSidePosition='false' if dualSidePosition else 'true',
                    recvWindow=30000)
    assert response.status == 200, response
    response = func(dualSidePosition=dualSidePosition, recvWindow=30000)
    assert response.status == 200, response
