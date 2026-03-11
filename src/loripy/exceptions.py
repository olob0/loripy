class LoripyError(Exception):
    pass


class NotFoundError(LoripyError):
    pass


class UnauthorizedError(LoripyError):
    pass


class RateLimitedError(LoripyError):
    pass
