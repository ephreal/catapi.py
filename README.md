Catapi.py
=========

[![PyPI version](https://badge.fury.io/py/catapi.svg)](https://badge.fury.io/py/catapi)

A python wrapper for TheCatAPI.com

Key Features
============

* Asynchronous: Perfect for discord bots


Installing
==========

**Python 3.5.3 or higher is REQUIRED. Python 3.5.3**

To install the library through pip

```
pip install catapi.py
```


Example usage
=============

catapi.py is written asynchronously, which requires using asyncio. While this is convenient when running a discord bot, it requires a little more setup in a script.

```
import asyncio
import catapi

# Create the event loop where the code executes
loop = asyncio.new_event_loop()

# Initialize the api
api = catapi.CatApi(api_key="YOUR_API_KEY_HERE")

def run_coro(coroutine):
    return loop.run_until_complete(coroutine)


results = run_coro(api.search(limit=1))
print(results[0].image.url)
```
