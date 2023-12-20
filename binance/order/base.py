"""
Order pydantic base models
"""
import json
from typing import TypeVar

from pydantic import BaseModel, conlist


class Order(BaseModel):
    """
    Order pydantic base class
    """

    class Config:
        use_enum_values = True


OrderType = TypeVar("OrderType", bound=Order)


class BatchOrder(BaseModel):
    """
    Batch order pydantic class
    """

    batchOrders: conlist(OrderType, min_length=1, max_length=5)

    def dict(self, *args, **kwargs):
        """
        Encodes batch order in correct binance format

        https://binance-docs.github.io/apidocs/futures/en/#place-multiple-orders-trade

        `/fapi/v1/batchOrders?batchOrders=[{"type":"LIMIT","timeInForce":"GTC","symbol":"BTCUSDT","side":"BUY","price":"10001","quantity":"0.001"}]`
        """
        orders = list()
        for order in self.batchOrders:
            d = order.dict(*args, **kwargs)
            # every value must be encoded as str (int and floats too)
            orders.append({k: str(v) for k, v in d.items()})
        return {"batchOrders": json.dumps(orders)}
