import asyncio
import time

from httpx import Headers


class RateLimiter:
    def __init__(self, enabled: bool = True):
        self.enabled = enabled
        self.lock = asyncio.Lock()
        self.reset_at = 0
        self.remaining = 1

    async def wait(self):
        if not self.enabled:
            return

        async with self.lock:
            now = time.time()

            if self.remaining <= 0 and now < self.reset_at:
                await asyncio.sleep(self.reset_at - now)

            self.remaining -= 1

    def update(self, headers: Headers):
        if not self.enabled:
            return

        self.remaining = int(headers.get("X-RateLimit-Remaining", 1))
        self.reset_at = float(headers.get("X-RateLimit-Reset", 0))
