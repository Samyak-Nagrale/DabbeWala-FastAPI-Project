from datetime import datetime
from enum import Enum

from sqlmodel import Field, SQLModel

"""Enum class to represent the status of an order."""


class OrderStatus(str, Enum):
    PREPARING = "preparing"
    PICKUP_UP = "picked_up"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"


"""Order Table that will store all the orders placed by customers."""


class Order(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    customer_name: str
    delivery_address: str
    items: str
    status: OrderStatus = Field(default=OrderStatus.PREPARING)
    created_at: datetime = Field(default_factory=datetime.timezone.now)
    updated_at: datetime = Field(default_factory=datetime.timezone.now)


"""OrderCreated schema, it's an pydantic model"""
"""Schema to represent the data required to create a new order."""


class OrderCreate(SQLModel):
    customer_name: str
    delivery_address: str
    items: str


"""OrderUpdated schema, it's an pydantic model"""
"""Schema to represent the data required to update an existing order."""


class OrderUpdateStatus(SQLModel):
    status: OrderStatus | None = None
    delivery_address: str | None = None


"""OrderResponse schema, it's an pydantic model"""
"""Track the old and new status of an order, along with the timestamp of the change"""


class StatusLog(SQLModel):
    order_id: int
    old_status: str
    new_status: str
    changed_at: datetime
