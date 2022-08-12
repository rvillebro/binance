"""
Market
======

All market data endpoints are collected here.

https://binance-docs.github.io/apidocs/futures/en/#market-data-endpoints

"""
from typing import Optional

from binance.client.endpoints.base import APIEndpoints, APIEndpointsLinkerMixin
from binance.client.response import Response  # must be imported directly as pydantic validate_arguments cant handle TYPE_CHECKING
from binance.enums.binance import KlineInterval, ContractType, Period  # must be imported directly as pydantic validate_arguments cant handle TYPE_CHECKING


class Market(APIEndpointsLinkerMixin):
    endpoints = APIEndpoints()

    @endpoints.add('GET', '/fapi/v1/ping')
    def ping() -> Response:
        """
        Pings server to test connectivity

        https://binance-docs.github.io/apidocs/futures/en/#test-connectivity

        Returns
        -------
        :class:`~binance.client.response.Response`
            Response from API call

        Examples
        --------
        To ping binance servers call:
            >>> client.market.ping()
            Response(status=200, data={})

        It is helpful to test connectivity and should return rather quickly.
        """

    @endpoints.add('GET', '/fapi/v1/time')
    def server_time() -> Response:
        """
        Gets current server time

        https://binance-docs.github.io/apidocs/futures/en/#check-server-time

        Returns
        -------
        :class:`binance.client.response.Response`
            Response from API call

        Examples
        --------
        To get binance server time call:

            >>> client.market.server_time()
            Response(status=200, data={'serverTime': ...})
        
        Your host time and Binance server time may vary.
        Remember that Binance uses UTC — Coordinated Universal Time.
        """

    @endpoints.add('GET', '/fapi/v1/exchangeInfo')
    def exchange_info() -> Response:
        """
        Gets current exchange trading rules and symbol information

        https://binance-docs.github.io/apidocs/futures/en/#exchange-information

        Returns
        -------
        :class:`binance.client.response.Response`
            Response from API call

        Examples
        --------
        To get Binance's exchange information call:

            >>> client.market.exchange_info()
            Response(status=200, data={'timezone': 'UTC', 'serverTime':...})

        Keep up to date with the exchange information in order to get the proper symbols etc.
        """

    @staticmethod
    @endpoints.add('GET', '/fapi/v1/depth')
    def order_book(symbol: str, limit: Optional[int] = None) -> Response:
        """
        Gets order book for a symbol.

        https://binance-docs.github.io/apidocs/futures/en/#order-book

        Parameters
        ----------
        symbol : str
            symbol to pull order book for
        limit : int, optional, optional
            limit the number of bids to return (default=500, valid limits:[5, 10, 20, 50, 100, 500, 1000])
        
        Returns
        -------
        :class:`binance.client.response.Response`
            Response from API call

        Examples
        --------
        To get the order book for a symbol call:

            >>> client.market.order_book(symbol='BTCUSDT')
            Response(status=200, data={'lastUpdateId':...})

        You are also able to limit the number of orders:

            >>> r = client.market.order_book(symbol='BTCUSDT', limit=5)
            >>> r.status
            200
            >>> len(r.data['bids'])
            5

        The limit can be set to the following interval: [5, 10, 20, 50, 100, 500, 1000]
        """

    @endpoints.add('GET', '/fapi/v1/trades')
    def recent_trades(symbol: str, limit: Optional[int] = None) -> Response:
        """
        Gets most recent trades for a symbol.

        https://binance-docs.github.io/apidocs/futures/en/#recent-trades-list

        Parameters
        ----------
        symbol : str
            symbol to pull recent trades for
        limit : int, optional, optional
            limit (default=500, max=1000)

        Returns
        -------
        :class:`binance.client.response.Response`
            Response from API call

        Examples
        --------
        To get recent trades call:

            >>> client.market.recent_trades(symbol='BTCUSDT')
            Response(status=200, data=[{'id': ...}])

        You are also able to limit the number of recent trades received:

            >>> r = client.market.recent_trades(symbol='BTCUSDT', limit=69)
            >>> r.status
            200
            >>> len(r.data)
            69

        The maximum limit is 1000.
        """

    @endpoints.add('GET', '/fapi/v1/historicalTrades', add_api_key=True)
    def historical_trades(symbol: str, limit: Optional[int] = None, fromId: Optional[int] = None) -> Response:
        """
        Gets historical trades for a symbol. (*MARKET_DATA*)

        * Market trades means trades filled in the order book.
        * Only market trades will be returned, which means the insurance fund trades and ADL trades won't be returned.

        https://binance-docs.github.io/apidocs/futures/en/#old-trades-lookup-market_data

        Parameters
        ----------
        symbol : str
            symbol to pull order book for.
        limit : int, optional, optional
            limit (default=500, max=1000)
        fromId : int, optional
            TradeId to fetch from. (default: most recent trades)
        
        Returns
        -------
        :class:`binance.client.response.Response`
            Response from API call

        Examples
        --------
        To get historical trades call:

            >>> client.market.historical_trades(symbol='BTCUSDT')
            Response(status=200, data=[...])
        
        You can limit the number of results:

            >>> r = client.market.historical_trades(symbol='BTCUSDT', limit=2)
            >>> r.status
            200
            >>> len(r.data)
            2

        And set from which ID to pull from:

            >>> from_id = r.data[0]['id']
            >>> r = client.market.historical_trades(symbol='BTCUSDT', fromId=from_id)
            >>> r.status
            200
            >>> r.data[0]['id'] == from_id
            True
        """

    @endpoints.add('GET', '/fapi/v1/aggTrades')
    def aggregated_trades(symbol: str,
                          fromId: Optional[int] = None,
                          startTime: Optional[int] = None,
                          endTime: Optional[int] = None,
                          limit: Optional[int] = None) -> Response:
        """
        Gets aggregate trades list for a symbol.

        * If both startTime and endTime are sent, time between startTime and endTime must be less than 1 hour.
        * If fromId, startTime, and endTime are not sent, the most recent aggregate trades will be returned.

        https://binance-docs.github.io/apidocs/futures/en/#compressed-aggregate-trades-list

        Parameters
        ----------
        symbol : str
            symbol to pull aggregated trades for
        fromId : int, optional
            from id
        startTime : int, optional, optional
            start time in seconds
        endTime : int, optional, optional
            end time in seconds
        limit : int, optional, optional
            limit (default=500, max=1000)

        Returns
        -------
        :class:`binance.client.response.Response`
            Response from API call
        """

    @endpoints.add('GET', '/fapi/v1/klines')
    def klines(symbol: str,
               interval: KlineInterval,
               startTime: Optional[int] = None,
               endTime: Optional[int] = None,
               limit: Optional[int] = None) -> Response:
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
        interval : :class:`binance.enums.binance.KlineInterval`, optional
            klines interval
        startTime : int, optional, optional
            start time in seconds
        endTime : int, optional, optional
            end time in seconds
        limit : int, optional, optional
            limit (default=500, max=1500)

        Returns
        -------
        :class:`binance.client.response.Response`
            Response from API call
        """

    @endpoints.add('GET', '/fapi/v1/continuousKlines')
    def continues_contract_klines(pair: str,
                                  contractType: ContractType,
                                  interval: KlineInterval,
                                  startTime: Optional[int] = None,
                                  endTime: Optional[int] = None,
                                  limit: Optional[int] = None) -> Response:
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
        contractType : :class:`binance.enums.binance.ContractType`
            contract type
        interval : :class:`binance.enums.binance.KlineInterval`
            interval
        startTime : int, optional, optional
            start time
        endTime : int, optional, optional
            end time
        limit : int, optional, optional
            limit (default=500, max=1500)

        Returns
        -------
        :class:`binance.client.response.Response`
            Response from API call
        """

    @endpoints.add('GET', '/fapi/v1/indexPriceKlines')
    def index_price_klines(pair: str,
                           interval: KlineInterval,
                           startTime: Optional[int] = None,
                           endTime: Optional[int] = None,
                           limit: Optional[int] = None) -> Response:
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
        interval : :class:`binance.enums.binance.KlineInterval`
            interval
        startTime : int, optional, optional
            start time
        endTime : int, optional, optional
            end time
        limit : int, optional, optional
            limit (default=500, max=1500)

        Returns
        -------
        :class:`binance.client.response.Response`
            Response from API call
        """


    @endpoints.add('GET', '/fapi/v1/markPriceKlines')
    def mark_price_klines(symbol: str,
                          interval: KlineInterval,
                          startTime: Optional[int] = None,
                          endTime: Optional[int] = None,
                          limit: Optional[int] = None) -> Response:
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
        interval : :class:`binance.enums.binance.KlineInterval`
            interval
        startTime : int, optional, optional
            start time
        endTime : int, optional, optional
            end time
        limit : int, optional, optional
            limit (default=500, max=1500)

        Returns
        -------
        :class:`binance.client.response.Response`
            Response from API call
        """

    @endpoints.add('GET', '/fapi/v1/premiumIndex')
    def mark_price(symbol: Optional[str] = None) -> Response:
        """
        Gets mark price for a symbol or all symbols.
        weight=1

        https://binance-docs.github.io/apidocs/futures/en/#mark-price

        Parameters
        ----------
        symbol : str, optional
            symbol

        Returns
        -------
        :class:`binance.client.response.Response`
            Response from API call
        """

    @endpoints.add('GET', '/fapi/v1/fundingRate')
    def funding_rate_history(symbol: str,
                             startTime: Optional[int] = None,
                             endTime: Optional[int] = None,
                             limit: Optional[int] = None) -> Response:
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
        startTime : int, optional, optional
            start time
        endTime : int, optional, optional
            end time
        limit : int, optional, optional
            limit (default: 100, max: 1000)

        Returns
        -------
        :class:`binance.client.response.Response`
            Response from API call
        """

    @endpoints.add('GET', '/fapi/v1/ticker/24hr')
    def ticker_price_change_statistics(symbol: Optional[str] = None) -> Response:
        """
        Gets the 24 hour rolling window price change statistics for symbol or all symbols.

        * If the symbol is not sent, tickers for all symbols will be returned in an array.

        https://binance-docs.github.io/apidocs/futures/en/#24hr-ticker-price-change-statistics

        Parameters
        ----------
        symbol : str, optional
            symbol to get 24 hour rolling window price change statistics for

        Returns
        -------
        :class:`binance.client.response.Response`
            Response from API call
        """

    @endpoints.add('GET', '/fapi/v1/ticker/price')
    def ticker_price(symbol: Optional[str] = None) -> Response:
        """
        Gets the latest price for a symbol or all symbols.

        * If the symbol is not sent, prices for all symbols will be returned in an array.

        https://binance-docs.github.io/apidocs/futures/en/#symbol-price-ticker

        Parameters
        ----------
        symbol : str, optional
            symbol
        """

    @endpoints.add('GET', '/fapi/v1/ticker/bookTicker')
    def ticker_order_book(symbol: Optional[str] = None) -> Response:
        """
        Gets best price/quantity on the order book for a symbol or all symbols.

        * If the symbol is not sent, bookTickers for all symbols will be returned in an array.

        https://binance-docs.github.io/apidocs/futures/en/#symbol-order-book-ticker

        Parameters
        ----------
        symbol : str, optional
            symbol

        Returns
        -------
        :class:`binance.client.response.Response`
            Response from API call
        """

    @endpoints.add('GET', '/fapi/v1/openInterest')
    def open_interest(symbol: str) -> Response:
        """
        Gets present open interest for a specific symbol.

        https://binance-docs.github.io/apidocs/futures/en/#open-interest

        Parameters
        ----------
        symbol : str
            symbol to present open interest for

        Returns
        -------
        :class:`binance.client.response.Response`
            Response from API call
        """

    @endpoints.add('GET', '/futures/data/openInterestHist')
    def open_interest_history(symbol: str,
                              period: Period,
                              limit: Optional[int] = None,
                              startTime: Optional[int] = None,
                              endTime: Optional[int] = None) -> Response:
        """
        Gets open interest history for a specific symbol.

        * If startTime and endTime are not sent, the most recent data is returned.
        * Only the data of the latest 30 days is available.

        https://binance-docs.github.io/apidocs/futures/en/#open-interest-statistics

        Parameters
        ----------
        symbol : str
            symbol to get funding rate history for
        period : :class:`binance.enums.binance.Period`
            period
        startTime : int, optional
            start time
        endTime : int, optional
            end time
        limit : int, optional
            limit (default: 30, max: 500)

        Returns
        -------
        :class:`binance.client.response.Response`
            Response from API call
        """

    @endpoints.add('GET',
                   '/futures/data/topLongShortAccountRatio',
                   add_api_key=True)
    def top_long_short_account_ratio(symbol: str,
                                     period: Period,
                                     limit: Optional[int] = None,
                                     startTime: Optional[int] = None,
                                     endTime: Optional[int] = None) -> Response:
        """
        Gets top trader long/short account ratio for a specific symbol.

        * If startTime and endTime are not sent, the most recent data is returned.
        * Only the data of the latest 30 days is available.

        https://binance-docs.github.io/apidocs/futures/en/#top-trader-long-short-ratio-accounts-market_data

        Parameters
        ----------
        symbol : str
            symbol to get funding rate history for
        period : :class:`binance.enums.binance.Period`
            period
        startTime : int, optional
            start time
        endTime : int, optional
            end time
        limit : int, optional
            limit (default: 30, max: 500)

        Returns
        -------
        :class:`binance.client.response.Response`
            Response from API call
        """

    @endpoints.add('GET', '/futures/data/topLongShortPositionRatio')
    def top_long_short_position_ratio(symbol: str,
                                      period: Period,
                                      limit: Optional[int] = None,
                                      startTime: Optional[int] = None,
                                      endTime: Optional[int] = None) -> Response:
        """
        Gets top trader long/short position ratio  a specific symbol.

        * If startTime and endTime are not sent, the most recent data is returned.
        * Only the data of the latest 30 days is available.

        https://binance-docs.github.io/apidocs/futures/en/#top-trader-long-short-ratio-positions

        Parameters
        ----------
        symbol : str
            symbol to get funding rate history for
        period : :class:`binance.enums.binance.Period`
            period
        startTime : int, optional
            start time
        endTime : int, optional
            end time
        limit : int, optional
            limit (default: 30, max: 500)

        Returns
        -------
        :class:`binance.client.response.Response`
            Response from API call
        """

    @endpoints.add('GET', '/futures/data/globalLongShortAccountRatio')
    def global_long_short_account_ratio(symbol: str,
                                        period: Period,
                                        limit: Optional[int] = None,
                                        startTime: Optional[int] = None,
                                        endTime: Optional[int] = None) -> Response:
        """
        Gets global long/short account ratio  a specific symbol.

        * If startTime and endTime are not sent, the most recent data is returned.
        * Only the data of the latest 30 days is available.

        https://binance-docs.github.io/apidocs/futures/en/#long-short-ratio

        Parameters
        ----------
        symbol : str
            symbol to get funding rate history for
        period : :class:`binance.enums.binance.Period`
            period
        startTime : int, optional
            start time
        endTime : int, optional
            end time
        limit : int, optional
            limit (default: 30, max: 500)

        Returns
        -------
        :class:`binance.client.response.Response`
            Response from API call
        """

    @endpoints.add('GET', '/futures/data/takerlongshortRatio')
    def taker_long_short_ratio(symbol: str,
                               period: Period,
                               limit: Optional[int] = None,
                               startTime: Optional[int] = None,
                               endTime: Optional[int] = None) -> Response:
        """
        Gets taker long/short ratio  a specific symbol.

        * If startTime and endTime are not sent, the most recent data is returned.
        * Only the data of the latest 30 days is available.

        https://binance-docs.github.io/apidocs/futures/en/#taker-buy-sell-volume

        Parameters
        ----------
        symbol : str
            symbol to get funding rate history for
        period : :class:`binance.enums.binance.Period`
            period
        startTime : int, optional
            start time
        endTime : int, optional
            end time
        limit : int, optional
            limit (default: 30, max: 500)

        Returns
        -------
        :class:`binance.client.response.Response`
            Response from API call
        """

    @endpoints.add('GET', '/fapi/v1/lvtKlines')
    def lvt_klines(symbol: str,
                   interval: KlineInterval,
                   startTime: Optional[int] = None,
                   endTime: Optional[int] = None,
                   limit: Optional[int] = None) -> Response:
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
        interval : :class:`binance.enums.binance.KlineInterval`
            klines interval
        startTime : int, optional
            start time in seconds
        endTime : int, optional
            end time in seconds
        limit : int, optional
            limit (default=500, max=1000)

        Returns
        -------
        :class:`binance.client.response.Response`
            Response from API call
        """

    @endpoints.add('GET', '/fapi/v1/indexInfo')
    def composite_index_info(symbol: Optional[str] = None) -> Response:
        """
        Gets mark price for a symbol or all symbols.
        * Only for composite index symbols

        https://binance-docs.github.io/apidocs/futures/en/#composite-index-symbol-information

        Parameters
        ----------
        symbol : str, optional
            symbol

        Returns
        -------
        :class:`binance.client.response.Response`
            Response from API call
        """

if __name__ == '__main__':
    import doctest
    from binance.client import Client
    doctest.testmod(globs=dict(client=Client()), optionflags=doctest.ELLIPSIS)
