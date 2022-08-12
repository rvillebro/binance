"""
"""
from typing import TypeVar
from pydantic import BaseModel, conlist

OrderType = TypeVar('OrderType', bound='Order')

class Order(BaseModel):
    """
    Order pydantic base class
    """
    class Config:
        use_enum_values = True


class BatchOrder(BaseModel):
    """
    Batch order pydantic class
    """
    batchOrders: conlist(OrderType, min_items=1, max_items=5)
