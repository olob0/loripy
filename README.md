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
import os
from asyncio import run

from dotenv import load_dotenv
from loripy import Client
from rich import print

load_dotenv()


TOKEN = os.getenv("TOKEN")


lori = Client(TOKEN)


async def main():
    user = await lori.users.get(123) # Discord user ID

    print(user)


run(main())
```
