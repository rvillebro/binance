"""
User Data Stream
================

https://binance-docs.github.io/apidocs/futures/en/#user-data-streams
"""
from binance.client.endpoints.base import Endpoints
from binance.client.response import Response

endpoints = Endpoints()


@endpoints.post("/fapi/v1/listenKey", add_api_key=True)
def get_listen_key() -> Response:
    """
    Gets a listen key for user data streams (USER_STREAM).

    https://binance-docs.github.io/apidocs/futures/en/#start-user-data-stream-user_stream

    Examples
    --------
    To get a listen key call:

        >>> client.user_data.get_listen_key()
        Response(status=200, data={'listenKey': ...})
    """


@endpoints.put("/fapi/v1/listenKey", add_api_key=True)
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


@endpoints.delete("DELETE", "/fapi/v1/listenKey", add_api_key=True)
def close_listen_key():
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


if __name__ == "__main__":
    import doctest

    from binance.client import Client

    doctest.testmod(globs=dict(client=Client()), optionflags=doctest.ELLIPSIS)
