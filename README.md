# Loripy

A very simple wrapper for the Loritta API.

> [!WARNING]
> I only implemented the endpoints that I needed.

## Installation

Use you favorite package manager. For example, pip:

```bash
pip install git+https://github.com/olob0/loripy.git
```

## Supported endpoints

- [x] get user info
- [x] get user transactions
- [ ] save a message using Loritta
- [ ] verify a saved message using Loritta
- [ ] create a giveaway
- [ ] end a giveaway
- [ ] reroll a giveaway
- [ ] request sonhos for a user
- [ ] transfer sonhos to a user
- [ ] get sonhos transaction status
- [ ] start a musical chairs event

## Usage

Example:

```python
# get user info

import os
from asyncio import run

from dotenv import load_dotenv
from loripy import Loritta
from rich import print # only for pretty printing

load_dotenv()


TOKEN = os.getenv("TOKEN")

if TOKEN is None:
    raise Exception("TOKEN is not set")


lori = Loritta(TOKEN)


async def main():
    user = await lori.users.get(123) # Discord user ID

    print(user)


run(main())
```

```python
# get user transactions

import asyncio
import datetime
import os

from dotenv import load_dotenv
from loripy import Loritta, TransactionType
from rich import print

load_dotenv()


async def main():
    TOKEN = os.getenv("TOKEN")

    if TOKEN is None:
        raise Exception("TOKEN is not set")

    lori = Loritta(TOKEN)

    before = datetime.datetime(year=2026, month=1, day=1)

    response = await lori.users.get_transactions(
        user_id=123,  # Discord user ID
        transaction_type=TransactionType.DAILY_REWARD,
        limit=2,
        before_date=before,
    )

    print(response)


if __name__ == "__main__":
    asyncio.run(main())

```
