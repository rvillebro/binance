"""
User Data Stream endpoints
==========================

https://binance-docs.github.io/apidocs/futures/en/#user-data-streams
"""
from .base import Endpoints, LinkEndpointsMixin


class UserData(LinkEndpointsMixin):
    endpoints = Endpoints()

    @endpoints.add('POST', '/fapi/v1/listenKey', add_api_key=True)
    def get_listen_key():
        """
        Gets a listen key for user data streams (USER_STREAM).

        https://binance-docs.github.io/apidocs/futures/en/#start-user-data-stream-user_stream

        Examples
        --------
        To get a listen key call:

            >>> client.user_data.get_listen_key()
            Response(status=200, data={'listenKey': ...})
        """

    @endpoints.add('PUT', '/fapi/v1/listenKey', add_api_key=True)
    def keep_listen_key_alive():
        """
        Keeps current listen key alive (USER_STREAM).

        https://binance-docs.github.io/apidocs/futures/en/#keepalive-user-data-stream-user_stream

        Examples
        --------
        To keep current user data streams listen key alive call:

            >>> client.user_data.keep_listen_key_alive()
            Response(status=200, data={})
        """

    @endpoints.add('DELETE', '/fapi/v1/listenKey', add_api_key=True)
    def close_list_key():
        """
        Closes current user data streams listen key (USER_STREAM).

        https://binance-docs.github.io/apidocs/futures/en/#close-user-data-stream-user_stream

        Examples
        --------
        Get a listen key:

            >>> client.user_data.get_listen_key()
            Response(status=200, data={'listenKey': ...})
        
        To close a listen key call:

            >>> client.user_data.close_list_key()
            Response(status=200, data={})
        """
