#!/usr/bin/env python3
"""
Market data endpoints

https://binance-docs.github.io/apidocs/futures/en/#market-data-endpoints
"""
from . import Endpoints

endpoints = Endpoints('market')

@endpoints.add('GET', '/fapi/v1/ping')
def ping():
    """
    Pings server to test connectivity

    https://binance-docs.github.io/apidocs/futures/en/#test-connectivity
    """
    pass


@endpoints.add('GET', '/fapi/v1/time')
async def server_time():
    """
    Gets current server time

    https://binance-docs.github.io/apidocs/futures/en/#check-server-time
    """
    pass


@endpoints.add('GET', '/fapi/v1/exchangeInfo')
async def exchange_info():
    """
    Gets current exchange trading rules and symbol information

    https://binance-docs.github.io/apidocs/futures/en/#exchange-information
    """
    pass


@endpoints.add('GET', '/fapi/v1/depth')
def order_book(symbol, limit=None):
    """
    Gets order book for a symbol.

    https://binance-docs.github.io/apidocs/futures/en/#order-book

    Parameters
    ----------
    symbol : str
        symbol to pull order book for
    limit : int
        limit (default=500, valid limits:[5, 10, 20, 50, 100, 500, 1000])
    """
    pass


@endpoints.add('GET', '/fapi/v1/trades')
async def recent_trades(symbol, limit=None):
    """
    Gets most recent trades for a symbol.

    https://binance-docs.github.io/apidocs/futures/en/#recent-trades-list

    Parameters
    ----------
    symbol : str
        symbol to pull recent trades for
    limit : int
        limit (default=500, max=1000)
    """
    pass


@endpoints.add('GET', '/fapi/v1/historicalTrades', add_api_key=True)
def historical_trades(symbol, limit=None, fromId=None):
    """
    Gets historical trades for a symbol. (*MARKET_DATA*)

    * Market trades means trades filled in the order book.
    * Only market trades will be returned, which means the insurance fund trades and ADL trades won't be returned.

    https://binance-docs.github.io/apidocs/futures/en/#old-trades-lookup-market_data

    Parameters
    ----------
    symbol : str
        symbol to pull order book for.
    limit : int, str
        limit (default=500, max=1000)
    fromId : int, str
        TradeId to fetch from. (default: most recent trades)
    """
    pass


@endpoints.add('GET', '/fapi/v1/aggTrades')
def aggregated_trades(symbol, fromId=None, startTime=None, endTime=None, limit=None):
    """
    Gets aggregate trades list for a symbol.

    * If both startTime and endTime are sent, time between startTime and endTime must be less than 1 hour.
    * If fromId, startTime, and endTime are not sent, the most recent aggregate trades will be returned.

    https://binance-docs.github.io/apidocs/futures/en/#compressed-aggregate-trades-list

    Parameters
    ----------
    symbol : str
        symbol to pull aggregated trades for
    fromId : int, str
        from id
    startTime : int, str
        start time in seconds
    endTime : int, str
        end time in seconds
    limit : int, str
        limit (default=500, max=1000)
    """
    pass


@endpoints.add('GET', '/fapi/v1/klines')
def klines(symbol, interval, startTime=None, endTime=None, limit=None):
    """
    Gets klines/candlesticks  for a symbol.

    * If startTime and endTime are not sent, the most recent klines are returned.
    * Klines are uniquely identified by their open time.
    * Weight: based on parameter limit

    https://binance-docs.github.io/apidocs/futures/en/#kline-candlestick-data

    Parameters
    ----------
    symbol : str
        symbol to pull klines/candlesticks for
    interval : binance.enums.binance.KlinesInterval
        klines interval
    startTime:
        start time in seconds
    endTime : int, str
        end time in seconds
    limit : int, str
        limit (default=500, max=1500)
    """
    pass


@endpoints.add('GET', '/fapi/v1/continuousKlines')
def continues_contract_klines(pair, contractType, interval, startTime=None, endTime=None, limit=None):
    """
    Gets continues contract klines/candlesticks for a pair.

    * If startTime and endTime are not sent, the most recent klines are returned.
    * Klines are uniquely identified by their open time.
    * Weight: based on parameter limit
    
    https://binance-docs.github.io/apidocs/futures/en/#continuous-contract-kline-candlestick-data

    Parameters
    ----------
    pair : str
        pair to pull continues klines/candlestick for
    contractType : binance.enums.binance.ContractTypes
        contract type
    interval : binance.enums.binance.KlinesInterval
        interval
    startTime : int
        start time
    endTime : int 
        end time
    limit : int
        limit (default=500, max=1500)
    """
    pass


@endpoints.add('GET', '/fapi/v1/indexPriceKlines')
def index_price_klines(pair, interval, startTime=None, endTime=None, limit=None):
    """
    Gets index price klines/candlesticks for a pair.

    * If startTime and endTime are not sent, the most recent klines are returned.
    * Klines are uniquely identified by their open time.
    * Weight: based on parameter limit

    https://binance-docs.github.io/apidocs/futures/en/#index-price-kline-candlestick-data
    
    Parameters
    ----------
    pair : str
        pair to pull continues klines/candlestick for
    contractType : binance.enums.binance.ContractTypes
        contract type
    interval : binance.enums.binance.KlinesInterval
        interval
    startTime : int
        start time
    endTime : int 
        end time
    limit : int
        limit (default=500, max=1500)
    """
    pass


@endpoints.add('GET', '/fapi/v1/markPriceKlines')
def mark_price_klines(symbol, interval, startTime=None, endTime=None, limit=None):
    """
    Gets mark price klines/candlesticks for a symbol.

    * If startTime and endTime are not sent, the most recent klines are returned.
    * Klines are uniquely identified by their open time.
    * Weight: based on parameter limit

    https://binance-docs.github.io/apidocs/futures/en/#mark-price-kline-candlestick-data

    Parameters
    ----------
    symbol : str
        symbol to pull continues klines/candlestick for
    contractType : binance.enums.binance.ContractTypes
        contract type
    interval : binance.enums.binance.KlinesInterval
        interval
    startTime : int
        start time
    endTime : int 
        end time
    limit : int
        limit (default=500, max=1500)
    """
    pass


@endpoints.add('GET', '/fapi/v1/premiumIndex')
def mark_price(symbol=None):
    """
    Gets mark price for a symbol or all symbols.
    weight=1

    https://binance-docs.github.io/apidocs/futures/en/#mark-price

    Parameters
    ----------
    symbol : str
        symbol
    """
    pass


@endpoints.add('GET', '/fapi/v1/fundingRate')
def funding_rate_history(symbol, startTime=None, endTime=None, limit=None):
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
        symbol to get funding rate history for
    startTime : int
        start time
    endTime : int
        end time
    limit : int
        limit (default: 100, max: 1000)
    """
    pass


@endpoints.add('GET', '/fapi/v1/ticker/24hr')
async def ticker_price_change_statistics(symbol=None):
    """
    Gets the 24 hour rolling window price change statistics for symbol or all symbols.

    * If the symbol is not sent, tickers for all symbols will be returned in an array.

    https://binance-docs.github.io/apidocs/futures/en/#24hr-ticker-price-change-statistics

    Parameters
    ----------
    symbol : str
        symbol to get 24 hour rolling window price change statistics for
    """
    pass


@endpoints.add('GET', '/fapi/v1/ticker/price')
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


@endpoints.add('GET', '/fapi/v1/ticker/bookTicker')
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


@endpoints.add('GET', '/fapi/v1/openInterest')
def open_interest(symbol):
    """
    Gets present open interest for a specific symbol.

    https://binance-docs.github.io/apidocs/futures/en/#open-interest

    Parameters
    ----------
    symbol : str
        symbol to present open interest for
    """
    pass


@endpoints.add('GET', '/futures/data/openInterestHist')
def open_interest_history(symbol, period, limit=None, startTime=None, endTime=None):
    """
    Gets open interest history for a specific symbol.

    * If startTime and endTime are not sent, the most recent data is returned.
    * Only the data of the latest 30 days is available.

    https://binance-docs.github.io/apidocs/futures/en/#open-interest-statistics

    Parameters
    ----------
    symbol : str
        symbol to get funding rate history for
    period : binance.enums.binance.Period
        period
    startTime : int
        start time
    endTime : int
        end time
    limit : int
        limit (default: 30, max: 500)
    """
    pass


@endpoints.add('GET', '/futures/data/topLongShortAccountRatio', add_api_key=True)
def top_long_short_account_ratio(symbol, period, limit=None, startTime=None, endTime=None):
    """
    Gets top trader long/short account ratio for a specific symbol.

    * If startTime and endTime are not sent, the most recent data is returned.
    * Only the data of the latest 30 days is available.

    https://binance-docs.github.io/apidocs/futures/en/#top-trader-long-short-ratio-accounts-market_data

    Parameters
    ----------
    symbol : str
        symbol to get funding rate history for
    period : binance.enums.binance.Period
        period
    startTime : int
        start time
    endTime : int
        end time
    limit : int
        limit (default: 30, max: 500)
    """
    pass


@endpoints.add('GET', '/futures/data/topLongShortPositionRatio')
def top_long_short_position_ratio(symbol, period, limit=None, startTime=None, endTime=None):
    """
    Gets top trader long/short position ratio  a specific symbol.

    * If startTime and endTime are not sent, the most recent data is returned.
    * Only the data of the latest 30 days is available.

    https://binance-docs.github.io/apidocs/futures/en/#top-trader-long-short-ratio-positions

    Parameters
    ----------
    symbol : str
        symbol to get funding rate history for
    period : binance.enums.binance.Period
        period
    startTime : int
        start time
    endTime : int
        end time
    limit : int
        limit (default: 30, max: 500)
    """
    pass


@endpoints.add('GET', '/futures/data/globalLongShortAccountRatio')
def global_long_short_account_ratio(symbol, period, limit=None, startTime=None, endTime=None):
    """
    Gets global long/short account ratio  a specific symbol.

    * If startTime and endTime are not sent, the most recent data is returned.
    * Only the data of the latest 30 days is available.

    https://binance-docs.github.io/apidocs/futures/en/#long-short-ratio

    Parameters
    ----------
    symbol : str
        symbol to get funding rate history for
    period : binance.enums.binance.Period
        period
    startTime : int
        start time
    endTime : int
        end time
    limit : int
        limit (default: 30, max: 500)
    """
    pass


@endpoints.add('GET', '/futures/data/takerlongshortRatio')
def taker_long_short_ratio(symbol, period, limit=None, startTime=None, endTime=None):
    """
    Gets taker long/short ratio  a specific symbol.

    * If startTime and endTime are not sent, the most recent data is returned.
    * Only the data of the latest 30 days is available.

    https://binance-docs.github.io/apidocs/futures/en/#taker-buy-sell-volume

    Parameters
    ----------
    symbol : str
        symbol to get funding rate history for
    period : binance.enums.binance.Period
        period
    startTime : int
        start time
    endTime : int
        end time
    limit : int
        limit (default: 30, max: 500)
    """
    pass


@endpoints.add('GET', '/fapi/v1/lvtKlines')
def lvt_klines(symbol, interval, startTime=None, endTime=None, limit=None):
    """
    Gets historical BLVT NAV klines/candlesticks for a symbol.

    * If startTime and endTime are not sent, the most recent klines are returned.
    * Klines are uniquely identified by their open time.
    * Weight: based on parameter limit

    https://binance-docs.github.io/apidocs/futures/en/#historical-blvt-nav-kline-candlestick

    Parameters
    ----------
    symbol : str
        symbol to pull historical BLVT NAV klines/candlesticks for
    interval : binance.enums.binance.KlinesInterval
        klines interval
    startTime:
        start time in seconds
    endTime : int, str
        end time in seconds
    limit : int, str
        limit (default=500, max=1000)
    """
    pass


@endpoints.add('GET', '/fapi/v1/indexInfo')
def composite_index_info(symbol=None):
    """
    Gets mark price for a symbol or all symbols.
    
    * Only for composite index symbols

    https://binance-docs.github.io/apidocs/futures/en/#composite-index-symbol-information

    Parameters
    ----------
    symbol : str
        symbol
    """
    pass