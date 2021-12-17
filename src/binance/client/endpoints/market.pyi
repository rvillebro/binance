"""
Market endpoints
================

https://binance-docs.github.io/apidocs/futures/en/#market-data-endpoints
"""
from typing import Any

class Market:
    def ping():
        """
        Pings server to test connectivity.

        https://binance-docs.github.io/apidocs/futures/en/#test-connectivity

        Examples
        --------
        To ping binance servers call:

            >>> client.market.ping()
            {'status_code': 200, 'response': {}}
        
        It should return rather quickly.
        It is helpful to test connectivity.
        """
        pass

    def server_time():
        """
        Gets current server time.

        https://binance-docs.github.io/apidocs/futures/en/#check-server-time

        Examples
        --------
        To get binance server time call:

            >>> client.market.server_time()
            {'status_code': 200, 'response': {'serverTime':...}}
        
        Your host time nad Binance server time may vary.
        Remeber that Binace uses UTC — Coordinated Universal Time.
        """
        pass

    def exchange_info():
        """
        Gets current exchange trading rules and symbol information.

        https://binance-docs.github.io/apidocs/futures/en/#exchange-information

        Examples
        --------
        To get Binance's exchange information call:

            >>> client.market.exchange_info()
            {'status_code': 200, 'response': {'timezone': 'UTC', 'serverTime':...}}
        
        Keep up to date with the exchange information in order to get the proper symbols etc.
        """
        pass

    def order_book(symbol, limit: int=None):
        """
        Gets order book for a symbol.

        https://binance-docs.github.io/apidocs/futures/en/#order-book

        Parameters
        ----------
        symbol : str
            symbol to pull order book for
        limit : int
            limit the number of bids to return (default=500, valid limits:[5, 10, 20, 50, 100, 500, 1000])
        
        Examples
        --------
        To get the order book for a symbol call:

            >>> client.market.order_book(symbol='BTCUSDT')
            {'status_code': 200, 'response': {'lastUpdateId':...}}
        
        You are also able to limit the number of orders:

            >>> r = client.market.order_book(symbol='BTCUSDT', limit=5)
            >>> len(r['response']['bids'])
            5
        
        The limit can be set in the following intervals: [5, 10, 20, 50, 100, 500, 1000]
        """
        pass

    def recent_trades(symbol, limit=None):
        """
        Gets most recent trades for a symbol.

        https://binance-docs.github.io/apidocs/futures/en/#recent-trades-list

        Parameters
        ----------
        symbol : str
            symbol to pull recent trades for
        limit : int
            limit (default=500, max=1000)
        
        Examples
        --------
        To get recent trades call:

            >>> client.market.recent_trades(symbol='BTCUSDT')
            {'status_code': 200, 'response': {'lastUpdateId':...}}
        """
        pass

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

    def ticker_price_change_statistics(symbol=None):
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
