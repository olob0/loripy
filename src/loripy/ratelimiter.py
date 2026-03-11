import asyncio
import time

from httpx import Headers


class RateLimiter:
    def __init__(self, enabled: bool = True):
        self.enabled = enabled
        self.lock = asyncio.Lock()
        self.reset_at = 0.0
        self.remaining = 1

    async def wait(self):
        if not self.enabled:
            return

        async with self.lock:
            now = time.time()

            if self.remaining <= 0:
                sleep_for = max(0.0, self.reset_at - now)
                if sleep_for > 0:
                    # margin
                    await asyncio.sleep(sleep_for + 0.05)

                self.remaining = 1

            self.remaining -= 1

    def update(self, headers: Headers):
        if not self.enabled:
            return

        reset_after = headers.get("X-RateLimit-Reset-After")
        if reset_after is not None:
            try:
                self.reset_at = time.time() + float(reset_after)
            except Exception:
                self.reset_at = float(headers.get("X-RateLimit-Reset", 0))  # fallback
        else:
            try:
                self.reset_at = float(headers.get("X-RateLimit-Reset", 0))
            except Exception:
                self.reset_at = 0.0

        try:
            self.remaining = max(0, int(headers.get("X-RateLimit-Remaining", 0)))
        except Exception:
            self.remaining = 0

        print(f"[debug] remaining: {self.remaining}, reset_at: {self.reset_at}")
