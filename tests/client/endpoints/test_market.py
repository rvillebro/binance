#!/usr/bin/env python3
from typing import TYPE_CHECKING

import pytest
from pydantic import ValidationError

if TYPE_CHECKING:
    from binance.client import Client


def test_ping(client: "Client"):
    assert client.market.ping().status == 200


def test_server_time(client: "Client"):
    assert client.market.server_time().status == 200


def test_exchange_info(client: "Client"):
    assert client.market.exchange_info().status == 200


def test_order_book(client: "Client"):
    assert client.market.order_book(symbol="BTCUSDT").status == 200

    r = client.market.order_book(symbol="BTCUSDT", limit=5)
    assert r.status == 200 and len(r.data["bids"]) == 5


def test_recent_trades(client: "Client"):
    assert client.market.recent_trades(symbol="BTCUSDT").status == 200

    r = client.market.recent_trades(symbol="BTCUSDT", limit=69)  # nice
    assert r.status == 200 and len(r.data) == 69  # nice


def test_historical_trades(client: "Client"):
    if client._api_key is None:
        pytest.skip("Requires API key!")

    assert client.market.historical_trades(symbol="BTCUSDT").status == 200

    r = client.market.historical_trades(symbol="BTCUSDT", limit=2)
    assert r.status == 200 and len(r.data) == 2

    from_id = r.data[0]["id"]
    r = client.market.historical_trades(symbol="BTCUSDT", limit=2, fromId=from_id)
    assert r.status == 200 and r.data[0]["id"] == from_id


def test_aggregated_trades(client: "Client"):
    func = client.market.aggregated_trades
    with pytest.raises(ValidationError):
        func()

    response = func(symbol="BTCUSDT")

    assert response.status == 200

    response = func(symbol="BTCUSDT", limit=1)
    assert response.status == 200

    from_id = response.data[0]["a"]
    response = func(symbol="BTCUSDT", fromId=from_id, limit=1)
    assert response.status == 200

    start_time = response.data[0]["T"]
    end_time = start_time + 1
    response = func(symbol="BTCUSDT", fromId=from_id, startTime=start_time)
    assert response.status == 200
    response = func(symbol="BTCUSDT", fromId=from_id, endTime=end_time)
    assert response.status == 200
    response = func(symbol="BTCUSDT", fromId=from_id, startTime=start_time, endTime=end_time)
    assert response.status == 200


def test_klines(client: "Client"):
    from binance.enums.binance import KlineInterval

    func = client.market.klines
    with pytest.raises(ValidationError):
        func()

    response = func(symbol="BTCUSDT", interval=KlineInterval.ONE_MINUTE)
    assert response.status == 200

    response = func(symbol="BTCUSDT", interval=KlineInterval.ONE_MINUTE, limit=1)
    assert response.status == 200

    startTime = response.data[0][0]
    endTime = startTime + 1000
    response = func(symbol="BTCUSDT", interval=KlineInterval.ONE_MINUTE, startTime=startTime)
    assert response.status == 200
    response = func(symbol="BTCUSDT", interval=KlineInterval.ONE_MINUTE, endTime=endTime)
    assert response.status == 200
    response = func(symbol="BTCUSDT", interval=KlineInterval.ONE_MINUTE, startTime=startTime, endTime=endTime)
    assert response.status == 200


def test_continues_contract_klines(client: "Client"):
    from binance.enums.binance import ContractType, KlineInterval

    func = client.market.continues_contract_klines
    with pytest.raises(ValidationError):
        func()

    response = func(pair="BTCUSDT", contractType=ContractType.PERPETUAL, interval=KlineInterval.ONE_MINUTE)
    assert response.status == 200

    response = func(pair="BTCUSDT", contractType=ContractType.PERPETUAL, interval=KlineInterval.ONE_MINUTE, limit=1)
    assert response.status == 200

    startTime = response.data[0][0]
    endTime = startTime + 1000
    response = func(
        pair="BTCUSDT", contractType=ContractType.PERPETUAL, interval=KlineInterval.ONE_MINUTE, startTime=startTime
    )
    assert response.status == 200
    response = func(
        pair="BTCUSDT", contractType=ContractType.PERPETUAL, interval=KlineInterval.ONE_MINUTE, endTime=endTime
    )
    assert response.status == 200
    response = func(
        pair="BTCUSDT",
        contractType=ContractType.PERPETUAL,
        interval=KlineInterval.ONE_MINUTE,
        startTime=startTime,
        endTime=endTime,
    )
    assert response.status == 200


def test_index_price_klines(client: "Client"):
    from binance.enums.binance import KlineInterval

    func = client.market.index_price_klines
    with pytest.raises(ValidationError):
        func()

    response = func(pair="BTCUSDT", interval=KlineInterval.ONE_MINUTE)
    assert response.status == 200

    response = func(pair="BTCUSDT", interval=KlineInterval.ONE_MINUTE, limit=1)
    assert response.status == 200

    startTime = response.data[0][0]
    endTime = startTime + 1000
    response = func(pair="BTCUSDT", interval=KlineInterval.ONE_MINUTE, startTime=startTime)
    assert response.status == 200
    response = func(pair="BTCUSDT", interval=KlineInterval.ONE_MINUTE, endTime=endTime)
    assert response.status == 200
    response = func(pair="BTCUSDT", interval=KlineInterval.ONE_MINUTE, startTime=startTime, endTime=endTime)
    assert response.status == 200


def test_mark_price_klines(client: "Client"):
    from binance.enums.binance import KlineInterval

    func = client.market.mark_price_klines
    with pytest.raises(ValidationError):
        func()

    response = func(symbol="BTCUSDT", interval=KlineInterval.ONE_MINUTE)
    assert response.status == 200

    response = func(symbol="BTCUSDT", interval=KlineInterval.ONE_MINUTE, limit=1)
    assert response.status == 200

    startTime = response.data[0][0]
    endTime = startTime + 1000
    response = func(symbol="BTCUSDT", interval=KlineInterval.ONE_MINUTE, startTime=startTime)
    assert response.status == 200
    response = func(symbol="BTCUSDT", interval=KlineInterval.ONE_MINUTE, endTime=endTime)
    assert response.status == 200
    response = func(symbol="BTCUSDT", interval=KlineInterval.ONE_MINUTE, startTime=startTime, endTime=endTime)
    assert response.status == 200


def test_mark_price(client: "Client"):
    func = client.market.mark_price
    response = func()
    assert response.status == 200

    response = func(symbol="BTCUSDT")
    assert response.status == 200


def test_funding_rate_history(client: "Client"):
    func = client.market.funding_rate_history
    with pytest.raises(ValidationError):
        func()

    response = func(symbol="BTCUSDT")
    assert response.status == 200

    start_time = response.data[0]["fundingTime"]
    end_time = start_time + 1
    response = func(symbol="BTCUSDT", startTime=start_time)
    assert response.status == 200
    response = func(symbol="BTCUSDT", endTime=end_time)
    assert response.status == 200
    response = func(symbol="BTCUSDT", startTime=start_time, endTime=end_time)
    assert response.status == 200


def test_ticker_price_change_statistics(client: "Client"):
    func = client.market.ticker_price_change_statistics
    response = func()
    assert response.status == 200

    response = func(symbol="BTCUSDT")
    assert response.status == 200


def test_ticker_price(client: "Client"):
    func = client.market.ticker_price
    response = func()
    assert response.status == 200

    response = func(symbol="BTCUSDT")
    assert response.status == 200


def test_ticker_order_book(client: "Client"):
    func = client.market.ticker_order_book
    response = func()
    assert response.status == 200

    response = func(symbol="BTCUSDT")
    assert response.status == 200


def test_open_interest(client: "Client"):
    pytest.skip("not working at the moment")

    func = client.market.open_interest

    with pytest.raises(ValidationError):
        func()

    response = func(symbol="BTCUSDT")
    assert response.status == 200


def test_open_interest_history(client: "Client"):
    pytest.skip("not working at the moment")
    from binance.enums.binance import Period

    func = client.market.open_interest_history
    with pytest.raises(ValidationError):
        func()

    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES)
    assert response.status == 200

    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES, limit=1)
    assert response.status == 200

    startTime = response.data[0]["timestamp"]
    endTime = startTime + 1000
    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES, startTime=startTime)
    assert response.status == 200
    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES, endTime=endTime)
    assert response.status == 200
    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES, startTime=startTime, endTime=endTime)
    assert response.status == 200


def test_top_long_short_account_ratio(client: "Client"):
    pytest.skip("not working at the moment")

    from binance.enums.binance import Period

    func = client.market.top_long_short_account_ratio
    with pytest.raises(ValidationError):
        func()

    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES)
    assert response.status == 200

    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES, limit=1)
    assert response.status == 200

    startTime = response.data[0]["timestamp"]
    endTime = startTime + 1000
    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES, startTime=startTime)
    assert response.status == 200
    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES, endTime=endTime)
    assert response.status == 200
    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES, startTime=startTime, endTime=endTime)
    assert response.status == 200


def test_top_long_short_position_ratio(client: "Client"):
    pytest.skip("not working at the moment")

    from binance.enums.binance import Period

    func = client.market.top_long_short_position_ratio
    with pytest.raises(ValidationError):
        func()

    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES)
    assert response.status == 200

    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES, limit=1)
    assert response.status == 200

    startTime = response.data[0]["timestamp"]
    endTime = startTime + 1000
    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES, startTime=startTime)
    assert response.status == 200
    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES, endTime=endTime)
    assert response.status == 200
    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES, startTime=startTime, endTime=endTime)
    assert response.status == 200


def test_global_long_short_account_ratio(client: "Client"):
    pytest.skip()

    from binance.enums.binance import Period

    func = client.market.global_long_short_account_ratio
    with pytest.raises(ValidationError):
        func()

    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES)
    assert response.status == 200

    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES, limit=1)
    assert response.status == 200

    startTime = response.data[0]["timestamp"]
    endTime = startTime + 1000
    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES, startTime=startTime)
    assert response.status == 200
    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES, endTime=endTime)
    assert response.status == 200
    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES, startTime=startTime, endTime=endTime)
    assert response.status == 200


def test_taker_long_short_ratio(client: "Client"):
    pytest.skip("not working at the moment")

    from binance.enums.binance import Period

    func = client.market.taker_long_short_ratio
    with pytest.raises(ValidationError):
        func()

    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES)
    assert response.status == 200

    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES, limit=1)
    assert response.status == 200

    startTime = response.data[0]["timestamp"]
    endTime = startTime + 1000
    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES, startTime=startTime)
    assert response.status == 200
    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES, endTime=endTime)
    assert response.status == 200
    response = func(symbol="BTCUSDT", period=Period.FIFTEEN_MINUTES, startTime=startTime, endTime=endTime)
    assert response.status == 200


def test_lvt_klines(client: "Client"):
    pytest.skip("not working at the moment")

    from binance.enums.binance import KlineInterval

    func = client.market.lvt_klines
    with pytest.raises(ValidationError):
        func()

    response = func(symbol="BLZUSDT", interval=KlineInterval.ONE_MINUTE)
    assert response.status == 200

    response = func(symbol="BLZUSDT", interval=KlineInterval.ONE_MINUTE, limit=1)
    assert response.status == 200

    startTime = response.data[0][0]
    endTime = startTime + 1000
    response = func(symbol="BLZUSDT", interval=KlineInterval.ONE_MINUTE, startTime=startTime)
    assert response.status == 200
    response = func(symbol="BLZUSDT", interval=KlineInterval.ONE_MINUTE, endTime=endTime)
    assert response.status == 200
    response = func(symbol="BLZUSDT", interval=KlineInterval.ONE_MINUTE, startTime=startTime, endTime=endTime)
    assert response.status == 200


def test_composite_index_info(client: "Client"):
    func = client.market.composite_index_info
    response = func()
    assert response.status == 200

    response = func(symbol="DEFIUSDT")
    assert response.status == 200
