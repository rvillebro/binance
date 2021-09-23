#!/usr/bin/env python3
import pytest


@pytest.mark.asyncio
async def test_ping(client):
    response = await client.market.ping()
    assert response['status_code'] == 200


@pytest.mark.asyncio
async def test_server_time(client):
    response = await client.market.server_time()
    assert response['status_code'] == 200


@pytest.mark.asyncio
async def test_exchange_info(client):
    response = await client.market.exchange_info()
    print(response)
    assert response['status_code'] == 200


@pytest.mark.asyncio
async def test_order_book(client):
    func = client.market.order_book
    with pytest.raises(TypeError, match=r"missing a required argument: 'symbol'"):
        await func()
    
    response = await func(symbol='BTCUSDT', limit=420)
    assert response['status_code'] == 400

    response = await func(symbol='BTCUSDT')
    assert response['status_code'] == 200

    response = await func(symbol='BTCUSDT', limit=5)
    assert response['status_code'] == 200


@pytest.mark.asyncio
async def test_recent_trades(client):
    func = client.market.recent_trades
    with pytest.raises(TypeError, match=r"missing a required argument: 'symbol'"):
        await func()

    response = await func(symbol='BTCUSDT')
    assert response['status_code'] == 200

    response = await func(symbol='BTCUSDT', limit=1)
    assert response['status_code'] == 200


@pytest.mark.asyncio
async def test_historical_trades(client):
    print(client._api_key)
    if client._api_key is None:
        pytest.skip("Requires API key!")

    func = client.market.historical_trades
    with pytest.raises(TypeError, match=r"missing a required argument: 'symbol'"):
        await func()

    response = await func(symbol='BTCUSDT')
    assert response['status_code'] == 200

    response = await func(symbol='BTCUSDT', limit=1)
    assert response['status_code'] == 200

    from_id = response['response'][0]['id']
    response = await func(symbol='BTCUSDT', limit=1, fromId=from_id)
    assert response['status_code'] == 200

@pytest.mark.asyncio
async def test_aggregated_trades(client):
    func = client.market.aggregated_trades
    with pytest.raises(TypeError, match=r"missing a required argument: 'symbol'"):
        await func()

    response = await func(symbol='BTCUSDT')
    assert response['status_code'] == 200
    
    response = await func(symbol='BTCUSDT', limit=1)
    assert response['status_code'] == 200
    
    from_id = response['response'][0]['a']
    response = await func(symbol='BTCUSDT', fromId=from_id, limit=1)
    assert response['status_code'] == 200

    start_time = response['response'][0]['T']
    end_time = start_time + 1
    response = await func(symbol='BTCUSDT', fromId=from_id, startTime=start_time)
    assert response['status_code'] == 200
    response = await func(symbol='BTCUSDT', fromId=from_id, endTime=end_time)
    assert response['status_code'] == 200
    response = await func(symbol='BTCUSDT', fromId=from_id, startTime=start_time, endTime=end_time)
    assert response['status_code'] == 200


@pytest.mark.asyncio
async def test_klines(client):
    from binance.enums.binance import KlineInterval

    func = client.market.klines
    with pytest.raises(TypeError, match=r"missing a required argument: 'symbol'"):
        await func()
    
    with pytest.raises(TypeError, match=r"missing a required argument: 'interval'"):
        await func(symbol='BTCUSDT')
    
    response = await func(symbol='BTCUSDT', interval=KlineInterval.ONE_MINUTE)
    assert response['status_code'] == 200

    response = await func(symbol='BTCUSDT', interval=KlineInterval.ONE_MINUTE, limit=1)
    assert response['status_code'] == 200

    startTime = response['response'][0][0]
    endTime = startTime + 1000
    response = await func(symbol='BTCUSDT', interval=KlineInterval.ONE_MINUTE, startTime=startTime)
    assert response['status_code'] == 200
    response = await func(symbol='BTCUSDT', interval=KlineInterval.ONE_MINUTE, endTime=endTime)
    assert response['status_code'] == 200
    response = await func(symbol='BTCUSDT', interval=KlineInterval.ONE_MINUTE, startTime=startTime, endTime=endTime)
    assert response['status_code'] == 200


@pytest.mark.asyncio
async def test_continues_contract_klines(client):
    from binance.enums.binance import ContractType, KlineInterval

    func = client.market.continues_contract_klines
    with pytest.raises(TypeError, match=r"missing a required argument: 'pair'"):
        await func()
    
    with pytest.raises(TypeError, match=r"missing a required argument: 'contractType'"):
        await func(pair='BTCUSDT')
    
    with pytest.raises(TypeError, match=r"missing a required argument: 'interval'"):
        await func(pair='BTCUSDT', contractType=ContractType.PERPETUAL)

    response = await func(pair='BTCUSDT', contractType=ContractType.PERPETUAL, interval=KlineInterval.ONE_MINUTE)
    assert response['status_code'] == 200

    response = await func(pair='BTCUSDT', contractType=ContractType.PERPETUAL, interval=KlineInterval.ONE_MINUTE, limit=1)
    assert response['status_code'] == 200

    startTime = response['response'][0][0]
    endTime = startTime + 1000
    response = await func(pair='BTCUSDT', contractType=ContractType.PERPETUAL, interval=KlineInterval.ONE_MINUTE, startTime=startTime)
    assert response['status_code'] == 200
    response = await func(pair='BTCUSDT', contractType=ContractType.PERPETUAL, interval=KlineInterval.ONE_MINUTE, endTime=endTime)
    assert response['status_code'] == 200
    response = await func(pair='BTCUSDT', contractType=ContractType.PERPETUAL, interval=KlineInterval.ONE_MINUTE, startTime=startTime, endTime=endTime)
    assert response['status_code'] == 200


@pytest.mark.asyncio
async def test_index_price_klines(client):
    from binance.enums.binance import KlineInterval

    func = client.market.index_price_klines
    with pytest.raises(TypeError, match=r"missing a required argument: 'pair'"):
        await func()
    
    with pytest.raises(TypeError, match=r"missing a required argument: 'interval'"):
        await func(pair='BTCUSDT')
    
    response = await func(pair='BTCUSDT', interval=KlineInterval.ONE_MINUTE)
    assert response['status_code'] == 200

    response = await func(pair='BTCUSDT', interval=KlineInterval.ONE_MINUTE, limit=1)
    assert response['status_code'] == 200

    startTime = response['response'][0][0]
    endTime = startTime + 1000
    response = await func(pair='BTCUSDT', interval=KlineInterval.ONE_MINUTE, startTime=startTime)
    assert response['status_code'] == 200
    response = await func(pair='BTCUSDT', interval=KlineInterval.ONE_MINUTE, endTime=endTime)
    assert response['status_code'] == 200
    response = await func(pair='BTCUSDT', interval=KlineInterval.ONE_MINUTE, startTime=startTime, endTime=endTime)
    assert response['status_code'] == 200


@pytest.mark.asyncio
async def test_mark_price_klines(client):
    from binance.enums.binance import KlineInterval

    func = client.market.mark_price_klines
    with pytest.raises(TypeError, match=r"missing a required argument: 'symbol'"):
        await func()
    
    with pytest.raises(TypeError, match=r"missing a required argument: 'interval'"):
        await func(symbol='BTCUSDT')
    
    response = await func(symbol='BTCUSDT', interval=KlineInterval.ONE_MINUTE)
    assert response['status_code'] == 200

    response = await func(symbol='BTCUSDT', interval=KlineInterval.ONE_MINUTE, limit=1)
    assert response['status_code'] == 200

    startTime = response['response'][0][0]
    endTime = startTime + 1000
    response = await func(symbol='BTCUSDT', interval=KlineInterval.ONE_MINUTE, startTime=startTime)
    assert response['status_code'] == 200
    response = await func(symbol='BTCUSDT', interval=KlineInterval.ONE_MINUTE, endTime=endTime)
    assert response['status_code'] == 200
    response = await func(symbol='BTCUSDT', interval=KlineInterval.ONE_MINUTE, startTime=startTime, endTime=endTime)
    assert response['status_code'] == 200


@pytest.mark.asyncio
async def test_mark_price(client):
    func = client.market.mark_price
    response = await func()
    assert response['status_code'] == 200

    response = await func(symbol='BTCUSDT')
    assert response['status_code'] == 200


@pytest.mark.asyncio
async def test_funding_rate_history(client):
    func = client.market.funding_rate_history
    with pytest.raises(TypeError, match=r"missing a required argument: 'symbol'"):
        await func()

    response = await func(symbol='BTCUSDT')
    assert response['status_code'] == 200

    start_time = response['response'][0]['fundingTime']
    end_time = start_time + 1
    response = await func(symbol='BTCUSDT', startTime=start_time)
    assert response['status_code'] == 200
    response = await func(symbol='BTCUSDT', endTime=end_time)
    assert response['status_code'] == 200
    response = await func(symbol='BTCUSDT', startTime=start_time, endTime=end_time)
    assert response['status_code'] == 200


@pytest.mark.asyncio
async def test_ticker_price_change_statistics(client):
    func = client.market.ticker_price_change_statistics
    response = await func()
    assert response['status_code'] == 200

    response = await func(symbol='BTCUSDT')
    assert response['status_code'] == 200


@pytest.mark.asyncio
async def test_ticker_price(client):
    func = client.market.ticker_price
    response = await func()
    assert response['status_code'] == 200

    response = await func(symbol='BTCUSDT')
    assert response['status_code'] == 200


@pytest.mark.asyncio
async def test_ticker_order_book(client):
    func = client.market.ticker_order_book
    response = await func()
    assert response['status_code'] == 200

    response = await func(symbol='BTCUSDT')
    assert response['status_code'] == 200


@pytest.mark.asyncio
async def test_open_interest(client):
    func = client.market.open_interest

    with pytest.raises(TypeError, match=r"missing a required argument: 'symbol'"):
        await func()

    response = await func(symbol='BTCUSDT')
    print(response)
    assert response['status_code'] == 200


@pytest.mark.asyncio
async def open_interest_history(client):
    """
    CURRENTLY NOT WORING IN TEST?
    """
    from binance.enums.binance import Period

    func = client.market.open_interest_history
    with pytest.raises(TypeError, match=r"missing a required argument: 'symbol'"):
        await func()
    
    with pytest.raises(TypeError, match=r"missing a required argument: 'period'"):
        await func(symbol='BTCUSDT')
    
    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES)
    assert response['status_code'] == 200

    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, limit=1)
    assert response['status_code'] == 200

    startTime = response['response'][0]['timestamp']
    endTime = startTime + 1000
    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, startTime=startTime)
    assert response['status_code'] == 200
    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, endTime=endTime)
    assert response['status_code'] == 200
    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, startTime=startTime, endTime=endTime)
    assert response['status_code'] == 200


@pytest.mark.asyncio
async def top_long_short_account_ratio(client):
    """
    CURRENTLY NOT WORING IN TEST?
    """
    from binance.enums.binance import Period

    func = client.market.top_long_short_account_ratio
    with pytest.raises(TypeError, match=r"missing a required argument: 'symbol'"):
        await func()
    
    with pytest.raises(TypeError, match=r"missing a required argument: 'period'"):
        await func(symbol='BTCUSDT')
    
    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES)
    assert response['status_code'] == 200

    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, limit=1)
    assert response['status_code'] == 200

    startTime = response['response'][0]['timestamp']
    endTime = startTime + 1000
    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, startTime=startTime)
    assert response['status_code'] == 200
    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, endTime=endTime)
    assert response['status_code'] == 200
    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, startTime=startTime, endTime=endTime)
    assert response['status_code'] == 200


@pytest.mark.asyncio
async def top_long_short_position_ratio(client):
    """
    CURRENTLY NOT WORING IN TEST?
    """
    from binance.enums.binance import Period

    func = client.market.top_long_short_position_ratio
    with pytest.raises(TypeError, match=r"missing a required argument: 'symbol'"):
        await func()
    
    with pytest.raises(TypeError, match=r"missing a required argument: 'period'"):
        await func(symbol='BTCUSDT')
    
    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES)
    assert response['status_code'] == 200

    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, limit=1)
    assert response['status_code'] == 200

    startTime = response['response'][0]['timestamp']
    endTime = startTime + 1000
    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, startTime=startTime)
    assert response['status_code'] == 200
    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, endTime=endTime)
    assert response['status_code'] == 200
    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, startTime=startTime, endTime=endTime)
    assert response['status_code'] == 200


@pytest.mark.asyncio
async def global_long_short_account_ratio(client):
    """
    CURRENTLY NOT WORING IN TEST?
    """
    from binance.enums.binance import Period

    func = client.market.global_long_short_account_ratio
    with pytest.raises(TypeError, match=r"missing a required argument: 'symbol'"):
        await func()
    
    with pytest.raises(TypeError, match=r"missing a required argument: 'period'"):
        await func(symbol='BTCUSDT')
    
    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES)
    assert response['status_code'] == 200

    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, limit=1)
    assert response['status_code'] == 200

    startTime = response['response'][0]['timestamp']
    endTime = startTime + 1000
    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, startTime=startTime)
    assert response['status_code'] == 200
    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, endTime=endTime)
    assert response['status_code'] == 200
    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, startTime=startTime, endTime=endTime)
    assert response['status_code'] == 200


@pytest.mark.asyncio
async def taker_long_short_ratio(client):
    """
    CURRENTLY NOT WORING IN TEST?
    """
    from binance.enums.binance import Period

    func = client.market.taker_long_short_ratio
    with pytest.raises(TypeError, match=r"missing a required argument: 'symbol'"):
        await func()
    
    with pytest.raises(TypeError, match=r"missing a required argument: 'period'"):
        await func(symbol='BTCUSDT')
    
    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES)
    assert response['status_code'] == 200

    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, limit=1)
    assert response['status_code'] == 200

    startTime = response['response'][0]['timestamp']
    endTime = startTime + 1000
    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, startTime=startTime)
    assert response['status_code'] == 200
    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, endTime=endTime)
    assert response['status_code'] == 200
    response = await func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, startTime=startTime, endTime=endTime)
    assert response['status_code'] == 200


@pytest.mark.asyncio
async def lvt_klines(client):
    """
    CURRENTLY NOT WORING IN TEST?
    """
    from binance.enums.binance import KlineInterval

    func = client.market.lvt_klines
    with pytest.raises(TypeError, match=r"missing a required argument: 'symbol'"):
        await func()
    
    with pytest.raises(TypeError, match=r"missing a required argument: 'interval'"):
        await func(symbol='BLZUSDT')
    
    response = await func(symbol='BLZUSDT', interval=KlineInterval.ONE_MINUTE)
    assert response['status_code'] == 200

    response = await func(symbol='BLZUSDT', interval=KlineInterval.ONE_MINUTE, limit=1)
    assert response['status_code'] == 200

    startTime = response['response'][0][0]
    endTime = startTime + 1000
    response = await func(symbol='BLZUSDT', interval=KlineInterval.ONE_MINUTE, startTime=startTime)
    assert response['status_code'] == 200
    response = await func(symbol='BLZUSDT', interval=KlineInterval.ONE_MINUTE, endTime=endTime)
    assert response['status_code'] == 200
    response = await func(symbol='BLZUSDT', interval=KlineInterval.ONE_MINUTE, startTime=startTime, endTime=endTime)
    assert response['status_code'] == 200


@pytest.mark.asyncio
async def test_composite_index_info(client):
    func = client.market.composite_index_info
    response = await func()
    assert response['status_code'] == 200

    response = await func(symbol='DEFIUSDT')
    assert response['status_code'] == 200
