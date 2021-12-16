#!/usr/bin/env python3
import pytest
from binance.client import Client

@pytest.fixture(autouse=True, scope='module')
def add_np(doctest_namespace, request):
    client = Client()
    doctest_namespace["client"] = client

    def close_client():
        client.close()
    
    request.addfinalizer(close_client)
