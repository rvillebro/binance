#!/usr/bin/env python3
import pytest
from pydantic import ValidationError


def test_aggregated_trades(client):
    func = client.market.aggregated_trades
    with pytest.raises(ValidationError):
        func()

    response = func(symbol='BTCUSDT')
    assert response['status_code'] == 200

    response = func(symbol='BTCUSDT', limit=1)
    assert response['status_code'] == 200

    from_id = response['response'][0]['a']
    response = func(symbol='BTCUSDT', fromId=from_id, limit=1)
    assert response['status_code'] == 200

    start_time = response['response'][0]['T']
    end_time = start_time + 1
    response = func(symbol='BTCUSDT', fromId=from_id, startTime=start_time)
    assert response['status_code'] == 200
    response = func(symbol='BTCUSDT', fromId=from_id, endTime=end_time)
    assert response['status_code'] == 200
    response = func(symbol='BTCUSDT',
                    fromId=from_id,
                    startTime=start_time,
                    endTime=end_time)
    assert response['status_code'] == 200


def test_klines(client):
    from binance.enums.binance import KlineInterval

    func = client.market.klines
    with pytest.raises(ValidationError):
        func()

    response = func(symbol='BTCUSDT', interval=KlineInterval.ONE_MINUTE)
    assert response['status_code'] == 200

    response = func(symbol='BTCUSDT',
                    interval=KlineInterval.ONE_MINUTE,
                    limit=1)
    assert response['status_code'] == 200

    startTime = response['response'][0][0]
    endTime = startTime + 1000
    response = func(symbol='BTCUSDT',
                    interval=KlineInterval.ONE_MINUTE,
                    startTime=startTime)
    assert response['status_code'] == 200
    response = func(symbol='BTCUSDT',
                    interval=KlineInterval.ONE_MINUTE,
                    endTime=endTime)
    assert response['status_code'] == 200
    response = func(symbol='BTCUSDT',
                    interval=KlineInterval.ONE_MINUTE,
                    startTime=startTime,
                    endTime=endTime)
    assert response['status_code'] == 200


def test_continues_contract_klines(client):
    from binance.enums.binance import ContractType, KlineInterval

    func = client.market.continues_contract_klines
    with pytest.raises(ValidationError):
        func()

    response = func(pair='BTCUSDT',
                    contractType=ContractType.PERPETUAL,
                    interval=KlineInterval.ONE_MINUTE)
    assert response['status_code'] == 200

    response = func(pair='BTCUSDT',
                    contractType=ContractType.PERPETUAL,
                    interval=KlineInterval.ONE_MINUTE,
                    limit=1)
    assert response['status_code'] == 200

    startTime = response['response'][0][0]
    endTime = startTime + 1000
    response = func(pair='BTCUSDT',
                    contractType=ContractType.PERPETUAL,
                    interval=KlineInterval.ONE_MINUTE,
                    startTime=startTime)
    assert response['status_code'] == 200
    response = func(pair='BTCUSDT',
                    contractType=ContractType.PERPETUAL,
                    interval=KlineInterval.ONE_MINUTE,
                    endTime=endTime)
    assert response['status_code'] == 200
    response = func(pair='BTCUSDT',
                    contractType=ContractType.PERPETUAL,
                    interval=KlineInterval.ONE_MINUTE,
                    startTime=startTime,
                    endTime=endTime)
    assert response['status_code'] == 200


def test_index_price_klines(client):
    from binance.enums.binance import KlineInterval

    func = client.market.index_price_klines
    with pytest.raises(ValidationError):
        func()

    response = func(pair='BTCUSDT', interval=KlineInterval.ONE_MINUTE)
    assert response['status_code'] == 200

    response = func(pair='BTCUSDT', interval=KlineInterval.ONE_MINUTE, limit=1)
    assert response['status_code'] == 200

    startTime = response['response'][0][0]
    endTime = startTime + 1000
    response = func(pair='BTCUSDT',
                    interval=KlineInterval.ONE_MINUTE,
                    startTime=startTime)
    assert response['status_code'] == 200
    response = func(pair='BTCUSDT',
                    interval=KlineInterval.ONE_MINUTE,
                    endTime=endTime)
    assert response['status_code'] == 200
    response = func(pair='BTCUSDT',
                    interval=KlineInterval.ONE_MINUTE,
                    startTime=startTime,
                    endTime=endTime)
    assert response['status_code'] == 200


def test_mark_price_klines(client):
    from binance.enums.binance import KlineInterval

    func = client.market.mark_price_klines
    with pytest.raises(ValidationError):
        func()

    response = func(symbol='BTCUSDT', interval=KlineInterval.ONE_MINUTE)
    assert response['status_code'] == 200

    response = func(symbol='BTCUSDT',
                    interval=KlineInterval.ONE_MINUTE,
                    limit=1)
    assert response['status_code'] == 200

    startTime = response['response'][0][0]
    endTime = startTime + 1000
    response = func(symbol='BTCUSDT',
                    interval=KlineInterval.ONE_MINUTE,
                    startTime=startTime)
    assert response['status_code'] == 200
    response = func(symbol='BTCUSDT',
                    interval=KlineInterval.ONE_MINUTE,
                    endTime=endTime)
    assert response['status_code'] == 200
    response = func(symbol='BTCUSDT',
                    interval=KlineInterval.ONE_MINUTE,
                    startTime=startTime,
                    endTime=endTime)
    assert response['status_code'] == 200


def test_mark_price(client):
    func = client.market.mark_price
    response = func()
    assert response['status_code'] == 200

    response = func(symbol='BTCUSDT')
    assert response['status_code'] == 200


def test_funding_rate_history(client):
    func = client.market.funding_rate_history
    with pytest.raises(ValidationError):
        func()

    response = func(symbol='BTCUSDT')
    assert response['status_code'] == 200

    start_time = response['response'][0]['fundingTime']
    end_time = start_time + 1
    response = func(symbol='BTCUSDT', startTime=start_time)
    assert response['status_code'] == 200
    response = func(symbol='BTCUSDT', endTime=end_time)
    assert response['status_code'] == 200
    response = func(symbol='BTCUSDT', startTime=start_time, endTime=end_time)
    assert response['status_code'] == 200


def test_ticker_price_change_statistics(client):
    func = client.market.ticker_price_change_statistics
    response = func()
    assert response['status_code'] == 200

    response = func(symbol='BTCUSDT')
    assert response['status_code'] == 200


def test_ticker_price(client):
    func = client.market.ticker_price
    response = func()
    assert response['status_code'] == 200

    response = func(symbol='BTCUSDT')
    assert response['status_code'] == 200


def test_ticker_order_book(client):
    func = client.market.ticker_order_book
    response = func()
    assert response['status_code'] == 200

    response = func(symbol='BTCUSDT')
    assert response['status_code'] == 200


def test_open_interest(client):
    pytest.skip("not working at the moment")

    func = client.market.open_interest

    with pytest.raises(ValidationError):
        func()

    response = func(symbol='BTCUSDT')
    assert response['status_code'] == 200


def test_open_interest_history(client):
    pytest.skip("not working at the moment")
    from binance.enums.binance import Period

    func = client.market.open_interest_history
    with pytest.raises(ValidationError):
        func()

    response = func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES)
    assert response['status_code'] == 200

    response = func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, limit=1)
    assert response['status_code'] == 200

    startTime = response['response'][0]['timestamp']
    endTime = startTime + 1000
    response = func(symbol='BTCUSDT',
                    period=Period.FIFTEEN_MINUTES,
                    startTime=startTime)
    assert response['status_code'] == 200
    response = func(symbol='BTCUSDT',
                    period=Period.FIFTEEN_MINUTES,
                    endTime=endTime)
    assert response['status_code'] == 200
    response = func(symbol='BTCUSDT',
                    period=Period.FIFTEEN_MINUTES,
                    startTime=startTime,
                    endTime=endTime)
    assert response['status_code'] == 200


def test_top_long_short_account_ratio(client):
    pytest.skip("not working at the moment")

    from binance.enums.binance import Period

    func = client.market.top_long_short_account_ratio
    with pytest.raises(ValidationError):
        func()

    response = func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES)
    assert response['status_code'] == 200

    response = func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, limit=1)
    assert response['status_code'] == 200

    startTime = response['response'][0]['timestamp']
    endTime = startTime + 1000
    response = func(symbol='BTCUSDT',
                    period=Period.FIFTEEN_MINUTES,
                    startTime=startTime)
    assert response['status_code'] == 200
    response = func(symbol='BTCUSDT',
                    period=Period.FIFTEEN_MINUTES,
                    endTime=endTime)
    assert response['status_code'] == 200
    response = func(symbol='BTCUSDT',
                    period=Period.FIFTEEN_MINUTES,
                    startTime=startTime,
                    endTime=endTime)
    assert response['status_code'] == 200


def test_top_long_short_position_ratio(client):
    pytest.skip("not working at the moment")

    from binance.enums.binance import Period

    func = client.market.top_long_short_position_ratio
    with pytest.raises(ValidationError):
        func()

    response = func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES)
    assert response['status_code'] == 200

    response = func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, limit=1)
    assert response['status_code'] == 200

    startTime = response['response'][0]['timestamp']
    endTime = startTime + 1000
    response = func(symbol='BTCUSDT',
                    period=Period.FIFTEEN_MINUTES,
                    startTime=startTime)
    assert response['status_code'] == 200
    response = func(symbol='BTCUSDT',
                    period=Period.FIFTEEN_MINUTES,
                    endTime=endTime)
    assert response['status_code'] == 200
    response = func(symbol='BTCUSDT',
                    period=Period.FIFTEEN_MINUTES,
                    startTime=startTime,
                    endTime=endTime)
    assert response['status_code'] == 200


def test_global_long_short_account_ratio(client):
    pytest.skip()

    from binance.enums.binance import Period

    func = client.market.global_long_short_account_ratio
    with pytest.raises(ValidationError):
        func()

    response = func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES)
    assert response['status_code'] == 200

    response = func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, limit=1)
    assert response['status_code'] == 200

    startTime = response['response'][0]['timestamp']
    endTime = startTime + 1000
    response = func(symbol='BTCUSDT',
                    period=Period.FIFTEEN_MINUTES,
                    startTime=startTime)
    assert response['status_code'] == 200
    response = func(symbol='BTCUSDT',
                    period=Period.FIFTEEN_MINUTES,
                    endTime=endTime)
    assert response['status_code'] == 200
    response = func(symbol='BTCUSDT',
                    period=Period.FIFTEEN_MINUTES,
                    startTime=startTime,
                    endTime=endTime)
    assert response['status_code'] == 200


def test_taker_long_short_ratio(client):
    pytest.skip("not working at the moment")

    from binance.enums.binance import Period

    func = client.market.taker_long_short_ratio
    with pytest.raises(ValidationError):
        func()

    response = func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES)
    assert response['status_code'] == 200

    response = func(symbol='BTCUSDT', period=Period.FIFTEEN_MINUTES, limit=1)
    assert response['status_code'] == 200

    startTime = response['response'][0]['timestamp']
    endTime = startTime + 1000
    response = func(symbol='BTCUSDT',
                    period=Period.FIFTEEN_MINUTES,
                    startTime=startTime)
    assert response['status_code'] == 200
    response = func(symbol='BTCUSDT',
                    period=Period.FIFTEEN_MINUTES,
                    endTime=endTime)
    assert response['status_code'] == 200
    response = func(symbol='BTCUSDT',
                    period=Period.FIFTEEN_MINUTES,
                    startTime=startTime,
                    endTime=endTime)
    assert response['status_code'] == 200


def test_lvt_klines(client):
    pytest.skip("not working at the moment")

    from binance.enums.binance import KlineInterval

    func = client.market.lvt_klines
    with pytest.raises(ValidationError):
        func()

    response = func(symbol='BLZUSDT', interval=KlineInterval.ONE_MINUTE)
    assert response['status_code'] == 200

    response = func(symbol='BLZUSDT',
                    interval=KlineInterval.ONE_MINUTE,
                    limit=1)
    assert response['status_code'] == 200

    startTime = response['response'][0][0]
    endTime = startTime + 1000
    response = func(symbol='BLZUSDT',
                    interval=KlineInterval.ONE_MINUTE,
                    startTime=startTime)
    assert response['status_code'] == 200
    response = func(symbol='BLZUSDT',
                    interval=KlineInterval.ONE_MINUTE,
                    endTime=endTime)
    assert response['status_code'] == 200
    response = func(symbol='BLZUSDT',
                    interval=KlineInterval.ONE_MINUTE,
                    startTime=startTime,
                    endTime=endTime)
    assert response['status_code'] == 200


def test_composite_index_info(client):
    func = client.market.composite_index_info
    response = func()
    assert response['status_code'] == 200

    response = func(symbol='DEFIUSDT')
    assert response['status_code'] == 200
