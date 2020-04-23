Catapi.py
=========

.. image:: https://img.shields.io/pypi/v/catapi.py.svg
   :target: https://pypi.python.org/pypi/catapi.py
   :alt: PyPI version info
.. image:: https://img.shields.io/pypi/pyversions/catapi.py.svg
   :target: https://pypi.python.org/pypi/catapi.py
   :alt: PyPI supported Python versions


A python wrapper for TheCatAPI.com

Key Features
------------

* Asynchronous: Perfect for discord bots


Installing
----------

**Python 3.5.3 or higher is REQUIRED.**

To install the library through pip

.. code:: sh

    pip install catapi.py


Example usage
-------------

catapi.py is written asynchronously, which requires using asyncio. While this is convenient when running a discord bot, it requires a little more setup in a script.

.. code:: sh

    import asyncio
    import catapi
    
    # Create the event loop where the code executes
    loop = asyncio.new_event_loop()
    
    # Initialize the api
    api = catapi.CatApi(api_key="YOUR_API_KEY_HERE")
    
    def run_coro(coroutine):
        return loop.run_until_complete(coroutine)
    
    
    results = run_coro(api.search(limit=1))
    print(results[0].url)
