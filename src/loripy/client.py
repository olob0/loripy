import httpx

from loripy.ratelimiter import RateLimiter
from loripy.requester import Requester
from loripy.routes.users import UsersRoute


class Client:
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.loritta.website/v1/",
        rate_limit_queue: bool = True,
        **kwargs,
    ):
        self.http = httpx.AsyncClient(
            base_url=base_url,
            headers={"Authorization": api_key},
            **kwargs,
        )

        self.ratelimiter = RateLimiter(rate_limit_queue)

        http = Requester(api_key, base_url)
        self.users = UsersRoute(http)
