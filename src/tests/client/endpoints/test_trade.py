#!/usr/bin/env python3
import pytest

@pytest.mark.asyncio
async def test_get_position_mode(client):
    response = await client.market.server_time()
    timestamp = response['response']['serverTime']
    response = await client.trade.get_position_mode(timestamp=timestamp)
    assert response['status_code'] == 200

@pytest.mark.asyncio
async def test_set_position_mode(client):
    func = client.trade.set_position_mode
    with pytest.raises(TypeError, match=r"missing a required argument: 'dualSidePosition'"):
        await func()
    
    response = await client.market.server_time()
    timestamp = response['response']['serverTime']
    response = await client.trade.get_position_mode(timestamp=timestamp)
    dualSidePosition = response['response']['dualSidePosition']
    response = await func(dualSidePosition=dualSidePosition, timestamp=timestamp)
    assert response['status_code'] == 400
    assert response['response']['code'] == -4059
    assert response['response']['msg'] == 'No need to change position side.'

    response = await func(dualSidePosition='true' if dualSidePosition=='false' else 'false', timestamp=timestamp)
    assert response['status_code'] == 200
    response = await func(dualSidePosition=dualSidePosition, timestamp=timestamp)
    assert response['status_code'] == 200
