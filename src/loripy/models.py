from datetime import datetime

from pydantic import BaseModel, Field

from loripy.enums import TransactionType


class Features(BaseModel):
    third_party_sonhos_transfer_tax: float = Field(alias="thirdPartySonhosTransferTax")


class User(BaseModel):
    id: int
    xp: int
    sonhos: int
    about_me: str | None = Field(default=None, alias="aboutMe")
    gender: str | None = None
    emoji_fight_emoji: str | None = Field(default=None, alias="emojiFightEmoji")
    loritta_ban_state: str | None = Field(default=None, alias="lorittaBanState")
    features: Features


class Transaction(BaseModel):
    type: str
    id: int
    transaction_type: TransactionType = Field(alias="transactionType")
    timestamp: datetime
    user: int
    sonhos: int


class Paging(BaseModel):
    total: int
    limit: int
    offset: int


class TransactionsResponse(BaseModel):
    transactions: list[Transaction]
    paging: Paging
