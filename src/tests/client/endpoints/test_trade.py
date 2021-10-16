#!/usr/bin/env python3
import pytest
import binance.utils

@pytest.mark.asyncio
async def test_get_position_mode(aioclient):
    if aioclient._api_key is None:
        pytest.skip("Requires API key!")

    response = await aioclient.trade.get_position_mode(recvWindow=30000)
    assert response['status_code'] == 200, response


@pytest.mark.asyncio
async def test_set_position_mode(aioclient):
    if aioclient._api_key is None and aioclient._api_secret is None:
        pytest.skip("Requires API key and secret!")
    
    func = aioclient.trade.set_position_mode
    with pytest.raises(TypeError, match=r"missing a required argument: 'dualSidePosition'"):
        await func()
    
    response = await aioclient.trade.get_position_mode(recvWindow=30000)
    assert response['status_code'] == 200, response

    dualSidePosition = response['response']['dualSidePosition']
    response = await func(dualSidePosition=dualSidePosition, recvWindow=30000)
    assert response['status_code'] == 400, response
    assert response['response']['code'] == -4059, response

    response = await func(dualSidePosition='false' if dualSidePosition else 'true', recvWindow=30000)
    assert response['status_code'] == 200, response
    response = await func(dualSidePosition=dualSidePosition, recvWindow=30000)
    assert response['status_code'] == 200, response
