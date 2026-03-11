from collections.abc import Iterable
from datetime import datetime

from loripy.enums import TransactionType
from loripy.models import TransactionsResponse, User
from loripy.requester import Requester


class UsersRoute:
    def __init__(self, http: Requester):
        self.http = http

    async def get(self, user_id: int) -> User:
        data = await self.http.request("GET", f"users/{user_id}")
        return User.model_validate(data)

    async def get_transactions(
        self,
        user_id: int,
        transaction_type: TransactionType | Iterable[TransactionType] | None = None,
        limit: int = 20,
        offset: int = 0,
        before_date: datetime | None = None,
        after_date: datetime | None = None,
    ) -> TransactionsResponse:

        if limit > 100:
            raise ValueError("Limit must be <= 100")

        if limit < 1:
            raise ValueError("Limit must be >= 1")

        if offset < 0:
            raise ValueError("Offset must be >= 0")

        params: dict[str, int | str] = {
            "limit": limit,
            "offset": offset,
        }

        if transaction_type:
            if isinstance(transaction_type, TransactionType):
                params["transactionTypes"] = transaction_type.value
            else:
                params["transactionTypes"] = ",".join(t.value for t in transaction_type)

        if before_date:
            params["beforeDate"] = before_date.isoformat()

        if after_date:
            params["afterDate"] = after_date.isoformat()

        data = await self.http.request(
            "GET",
            f"users/{user_id}/transactions",
            params=params,
        )

        return TransactionsResponse.model_validate(data)
