import httpx

from loripy.ratelimiter import RateLimiter


class Requester:
    def __init__(self, api_key: str, base_url: str):
        self.ratelimiter = RateLimiter()
        self.http = httpx.AsyncClient(
            base_url=base_url,
            headers={"Authorization": api_key},
        )

    async def request(self, url: str, method: str = "GET", **kwargs):
        await self.ratelimiter.wait()

        response = await self.http.request(method, url, **kwargs)

        self.ratelimiter.update(response.headers)

        response.raise_for_status()
        return response.json()
