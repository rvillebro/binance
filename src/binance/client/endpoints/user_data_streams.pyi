"""
User Data Stream endpoints
==========================

https://binance-docs.github.io/apidocs/futures/en/#user-data-streams
"""

class UserDataStreams:
    def get_listen_key():
        """
        Gets a listen key for user data streams (USER_STREAM).

        https://binance-docs.github.io/apidocs/futures/en/#start-user-data-stream-user_stream

        Examples
        --------
        To get a listen key call:

            >>> client.user_data_streams.get_listen_key()
            {'status_code': 200, 'response': {'listenKey': ...}}
        """

    def keep_listen_key_alive():
        """
        Keeps current listen key alive (USER_STREAM).

        https://binance-docs.github.io/apidocs/futures/en/#keepalive-user-data-stream-user_stream

        Examples
        --------
        To keep current user data streams listen key alive call:

            >>> client.user_data_streams.keep_listen_key_alive()
            {'status_code': 200, 'response': {}}
        """

    def close_list_key():
        """
        Closes current user data streams listen key (USER_STREAM).

        https://binance-docs.github.io/apidocs/futures/en/#close-user-data-stream-user_stream

        Examples
        --------
        To keep current listen key alive call:

            >>> client.user_data_streams.close_list_key()
            {'status_code': 200, 'response': {}}
        """
