#!/usr/bin/env python3.8
from . import Endpoints

endpoints = Endpoints('general')

@endpoints.get('/fapi/v1/ping')
def ping():
    """
    Pings server
    """
    pass
    
@endpoints.get('/fapi/v1/time')
async def server_time():
    """
    Gets server time
    """
    pass

@endpoints.get('/fapi/v1/exchangeInfo')
async def exchange_info():
    """
    Gets exchange information
    """
    pass
