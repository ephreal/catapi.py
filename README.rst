Catapi.py
=========

.. image:: https://img.shields.io/pypi/v/catapi.py.svg
   :target: https://pypi.python.org/pypi/catapi.py
   :alt: PyPI version info
.. image:: https://img.shields.io/pypi/pyversions/catapi.py.svg
   :target: https://pypi.python.org/pypi/catapi.py
   :alt: PyPI supported Python versions
.. image:: https://api.codacy.com/project/badge/Grade/e9356b6c98e4469d97e8be949b20209c
   :target: https://www.codacy.com/manual/ephreal/catapi.py?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ephreal/catapi.py&amp;utm_campaign=Badge_Grade
   :alt: View code quality on Codacy


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
