from pydantic import BaseModel, Field, field_validator
from typing import Literal

class BaseOrder(BaseModel):
    symbol: str = Field(..., min_length=1)
    side: Literal["BUY", "SELL"]
    quantity: float = Field(..., gt=0)

    @field_validator("symbol",mode="before")
    @classmethod
    def symbol_upper(cls, value):
        return value.upper()
    @field_validator("side",mode="before")
    @classmethod
    def side_upper(cls, value):
        return value.upper()


class MarketOrder(BaseOrder):
    pass


class LimitOrder(BaseOrder):
    price: float = Field(..., gt=0)