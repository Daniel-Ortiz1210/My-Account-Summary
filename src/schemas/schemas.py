from pydantic import BaseModel, Field
from typing import List


class TransactionSchema(BaseModel):
    id: str = Field(..., alias="Id")
    date: str = Field(..., alias="Date")
    transaction: float = Field(..., alias="Transaction")
    account_number: int = Field(...)


class TransactionsSchema(BaseModel):
    transactions: List[TransactionSchema]
    