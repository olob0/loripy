from typing import Literal

import httpx

from loripy.exceptions import (
    LoripyError,
    NotFoundError,
    RateLimitedError,
    UnauthorizedError,
)
from loripy.ratelimiter import RateLimiter

Methods = Literal["GET", "POST", "PUT", "DELETE"]


class Requester:
    def __init__(self, api_key: str, base_url: str):
        self.ratelimiter = RateLimiter()
        self.http = httpx.AsyncClient(
            base_url=base_url,
            headers={"Authorization": api_key},
        )

    async def request(self, method: Methods, url: str, **kwargs):
        await self.ratelimiter.wait()

        response = await self.http.request(method, url, **kwargs)

        self.ratelimiter.update(response.headers)

        if response.status_code == 404:
            raise NotFoundError(f"Resource not found: {url}")

        if response.status_code == 401:
            raise UnauthorizedError("Unauthorized")

        if response.status_code == 429:
            raise RateLimitedError("Rate limit exceeded")

        if response.is_error:
            raise LoripyError(f"API error {response.status_code}: {response.text}")

        response.raise_for_status()
        return response.json()
