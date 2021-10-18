#!/usr/bin/env python3
import pytest
from binance.client import Client

@pytest.fixture(scope='module')
def client():
    c = Client()
    yield c
    c.close()