#!/usr/bin/env python3
from . import Endpoints

endpoints = Endpoints('market')

@endpoints.get('/fapi/v1/depth')
def order_book(symbol, limit=None):
    """
    Gets the order book for a symbol.

    https://binance-docs.github.io/apidocs/futures/en/#order-book

    Args:
        symbol (str): symbol to pull order book for.
        limit (int): limit
    """
    pass


@endpoints.get('/fapi/v1/trades')
async def recent_trades(symbol, limit=None):
    """
    Gets most recent trades for a symbol.

    https://binance-docs.github.io/apidocs/futures/en/#recent-trades-list

    Args:
        symbol (str): symbol to pull order book for.
        limit (int): limit
    """
    pass

d = dict(
    from_id = 'fromId'
)
@endpoints.get('/fapi/v1/historicalTrades', api_key=True)
def historical_trades(symbol, limit=None, fromId=None):
    """
    Gets historical trades for a symbol. (*MARKET_DATA*)

    https://binance-docs.github.io/apidocs/futures/en/#old-trades-lookup-market_data

    Market trades means trades filled in the order book.
    Only market trades will be returned, which means the insurance fund trades and ADL trades won't be returned.

    Parameters
    ----------
    symbol : str
        symbol to pull order book for.
    limit : int
        Default 500; max 1000.
    from_id : str
        TradeId to fetch from. Default gets most recent trades.
    """
    pass

d = dict(
    from_id='fromId',
    start_time='startTime',
    end_time='endTime',
)
@endpoints.get('/fapi/v1/aggTrades')
def aggregated_trades(symbol, from_id=None, start_time=None, end_time=None, limit=None):
        """
        Gets aggregate trades list for a symbol.

        * If both start time and end time are sent, time between start time and end time must be less than 1 hour.
        * If from id, start time, and end time are not sent, the most recent aggregate trades will be returned.

        https://binance-docs.github.io/apidocs/futures/en/#compressed-aggregate-trades-list

        Args:
            symbol (str): symbol to pull order book for.
            from_id (str): from id.
            start_time: start time.
            end_time: end time.
            limit (int): limit.
        """
        pass

d = dict(
    start_time='startTime',
    end_time='endTime',
)
@endpoints.get('/fapi/v1/klines')
def klines(symbol, interval, start_time=None, end_time=None, limit=None):
    """
    Gets klines/bars for a symbol.

    * If start time and end time are not sent, the most recent klines are returned.

    https://binance-docs.github.io/apidocs/futures/en/#kline-candlestick-data

    Args:
        symbol (str): symbol to pull order book for.
        interval (Klines): interval.
        start_time: start time.
        end_time: end time.
        limit (int): limit.
    """
    pass


d = dict(
    start_time='startTime',
    end_time='endTime',
    contract_type='contractTime'
)
@endpoints.get('/fapi/v1/continuousKlines')
def continues_klines(symbol, contract_type, interval, start_time=None, end_time=None, limit=None):
    """
    Gets continues klines/bars for a symbol.

    * If startTime and endTime are not sent, the most recent klines are returned.
    * Contract types:
        * PERPETUAL
    
    https://binance-docs.github.io/apidocs/futures/en/#continues-contract-kline-candlestick-data

    Parameters
    ----------
    symbol : str
        symbol to pull order book for
    contract_type : ContractTypes
        contract type
    interval : KlinesInterval
        interval
    start_time : int
        start time
    end_time : int 
        end time
    limit : int
        limit
    """
    pass


@endpoints.get('/fapi/v1/premiumIndex')
def mark_price(symbol=None):
    """
    Gets mark price for a symbol or all symbols.

    https://binance-docs.github.io/apidocs/futures/en/#mark-price

    Parameters
    ----------
    symbol : str
        symbol
    """
    pass


d = dict(
    start_time='startTime',
    end_time='endTime',
)
@endpoints.get('/fapi/v1/fundingRate')
def funding_rate_history(symbol, start_time=None, end_time=None, limit=None):
    """
    Gets funding rate history.

    * If start time and end time are not sent, the most recent limit datas are returned.
    * If the number of data between start time and end time is larger than limit, return as startTime + limit.
    * In ascending order.

    weight: 1

    https://binance-docs.github.io/apidocs/futures/en/#get-funding-rate-history

    Parameters
    ----------
    symbol : str
        symbol
    start_time : int
        start time
    end_time : int
        end time
    limit : int
        limit (default: 100, max: 1000)
    """
    pass


@endpoints.get('/fapi/v1/ticker/24hr')
async def ticker_price_change_statistics(symbol=None):
    """
    Gets the 24 hour rolling window price change statistics for symbol or all symbols.

    * If the symbol is not sent, tickers for all symbols will be returned in an array.

    https://binance-docs.github.io/apidocs/futures/en/#24hr-ticker-price-change-statistics

    Parameters
    ----------
    symbol : str
        symbol
    """
    pass


@endpoints.get('/fapi/v1/ticker/price')
def ticker_price(symbol=None):
    """
    Gets the latest price for a symbol or all symbols.

    * If the symbol is not sent, prices for all symbols will be returned in an array.

    https://binance-docs.github.io/apidocs/futures/en/#symbol-price-ticker

    Parameters
    ----------
    symbol : str
        symbol
    """
    pass


@endpoints.get('/fapi/v1/ticker/bookTicker')
def ticker_order_book(symbol=None):
    """
    Gets best price/quantity on the order book for a symbol or all symbols.

    * If the symbol is not sent, bookTickers for all symbols will be returned in an array.

    https://binance-docs.github.io/apidocs/futures/en/#symbol-order-book-ticker

    Parameters
    ----------
    symbol : str
        symbol
    """
    pass


#async def liquidation_orders(symbol=None, start_time=None, end_time=None, limit=None):
#    """
#    Gets all liquidation orders for a symbol or all symbols.
#
#    * If the symbol is not sent, liquidation orders for all symbols will be returned.
#
#    https://binance-docs.github.io/apidocs/futures/en/#get-all-liquidation-orders
#
#    Args:
#        symbol:
#        start_time:
#        end_time:
#        limit:
#    """
#    params = utils.clean_params({
#        'symbol': symbol,
#        'startTime': start_time,
#        'endTime': end_time,
#        'limit': limit,
#    })
#
#    return await self._client._call(http.Call.GET, '/fapi/v1/allForceOrders', params=params)
#
#async def open_interest(symbol):
#    """
#    Gets open interest for a symbol.
#
#    https://binance-docs.github.io/apidocs/futures/en/#open-interest
#
#    Args:
#        symbol:
#    """
#    params = utils.clean_params({
#        'symbol': symbol,
#    })
#
#    return await self._client._call(http.Call.GET, '/fapi/v1/openInterest', params=params)
#
#async def open_interest_statistics(symbol, period, start_time=None, end_time=None, limit=None):
#    """
#    Gets open interest statistics for a symbol.
#
#    * If startTime and endTime are not sent, the most recent data is returned.
#    * Only the data of the latest 30 days is available.
#
#    https://binance-docs.github.io/apidocs/futures/en/#open-interest-statistics
#
#    Args:
#        symbol:
#        period:
#        start_time:
#        end_time:
#        limit:
#    """
#    params = utils.clean_params({
#        'symbol': symbol,
#        'period': period,
#        'limit': limit,
#        'startTime': start_time,
#        'endTime': end_time,
#    })
#
#    return await self._client._call(http.Call.GET, '/futures/data/openInterestHist', params=params)
#
#async def top_long_short_ratio_accounts(symbol, period, start_time=None, end_time=None, limit=None):
#    """
#    Gets top trader long/short ratio of accounts for a symbol. (*MARKET_DATA*)
#
#    * If start time and end time are not sent, the most recent data is returned.
#    * Only the data of the latest 30 days is available.
#
#    https://binance-docs.github.io/apidocs/futures/en/#top-trader-long-short-ratio-accounts-market_data
#
#    Args:
#        symbol:
#        period:
#        start_time:
#        end_time:
#        limit:
#    """
#    params = utils.clean_params({
#        'symbol': symbol,
#        'period': period,
#        'limit': limit,
#        'startTime': start_time,
#        'endTime': end_time,
#    })
#
#    return await self._client._call(http.Call.GET, '/futures/data/topLongShortAccountRatio', params=params, use_api_key=True)
#
#async def top_long_short_ratio_positions(symbol, period, start_time=None, end_time=None, limit=None):
#    """
#    Gets top trader long/short ratio of accounts for a symbol.
#
#    * If start time and end time are not sent, the most recent data is returned.
#    * Only the data of the latest 30 days is available.
#
#    https://binance-docs.github.io/apidocs/futures/en/#top-trader-long-short-ratio-positions
#
#    Args:
#        symbol:
#        period:
#        start_time:
#        end_time:
#        limit:
#    """
#    params = utils.clean_params({
#        'symbol': symbol,
#        'period': period,
#        'limit': limit,
#        'startTime': start_time,
#        'endTime': end_time,
#    })
#
#    return await self._client._call(http.Call.GET, '/futures/data/topLongShortPositionRatio', params=params)
#
#async def long_short_ratio_accounts(symbol, period, start_time=None, end_time=None, limit=None):
#    """
#    Gets global long/short ratio of accounts for a symbol.
#
#    * If start time and end time are not sent, the most recent data is returned.
#    * Only the data of the latest 30 days is available.
#
#    https://binance-docs.github.io/apidocs/futures/en/#long-short-ratio
#
#    Args:
#        symbol:
#        period:
#        start_time:
#        end_time:
#        limit:
#    """
#    params = utils.clean_params({
#        'symbol': symbol,
#        'period': period,
#        'limit': limit,
#        'startTime': start_time,
#        'endTime': end_time,
#    })
#
#    return await self._client._call(http.Call.GET, '/futures/data/globalLongShortAccountRatio', params=params)
#
#async def buy_sell_volume(symbol, period, start_time=None, end_time=None, limit=None):
#    """
#    Gets taker buy/sell volume statistics.
#
#    * If start time and end time are not sent, the most recent data is returned.
#    * Only the data of the latest 30 days is available.
#
#    https://binance-docs.github.io/apidocs/futures/en/#taker-buy-sell-volume
#
#    Args:
#        symbol:
#        period:
#        start_time:
#        end_time:
#        limit:
#    """
#    params = utils.clean_params({
#        'symbol': symbol,
#        'period': period,
#        'startTime': start_time,
#        'endTime': end_time,
#        'limit': limit,
#    })
#
#    return await self._client._call(http.Call.GET, '/futures/data/globalLongShortAccountRatio', params=params)