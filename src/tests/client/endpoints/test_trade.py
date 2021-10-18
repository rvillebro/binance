#!/usr/bin/env python3
import pytest

def test_get_position_mode(client):
    if client._api_key is None:
        pytest.skip("Requires API key!")

    response = client.trade.get_position_mode(recvWindow=30000)
    assert response['status_code'] == 200, response


def test_set_position_mode(client):
    if client._api_key is None and client._api_secret is None:
        pytest.skip("Requires API key and secret!")
    
    func = client.trade.set_position_mode
    with pytest.raises(TypeError, match=r"missing a required argument: 'dualSidePosition'"):
        func()
    
    response = client.trade.get_position_mode(recvWindow=30000)
    assert response['status_code'] == 200, response

    dualSidePosition = response['response']['dualSidePosition']
    response = func(dualSidePosition=dualSidePosition, recvWindow=30000)
    assert response['status_code'] == 400, response
    assert response['response']['code'] == -4059, response

    response = func(dualSidePosition='false' if dualSidePosition else 'true', recvWindow=30000)
    assert response['status_code'] == 200, response
    response = func(dualSidePosition=dualSidePosition, recvWindow=30000)
    assert response['status_code'] == 200, response
