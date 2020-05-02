Getting Started
===============

Request an api key for the catapi from https://thecatapi.com/signup

Once you have your api key, download and install catapi.py with pip

.. code:: sh

    pip install catapi.py

To set up the CatAPI with it's api key for use, pass in it's api key when creating the CatApi object

.. code:: python

    import catapi
    API_KEY = "Your-API-key-here"
    api = catapi.CatApi(API_KEY)

Because catapi.py is written asynchronously, you will need to also import asyncio if you intend to run this in a script. This is a simple asyncio wrapper you could pass in any catapi method and receive the result

.. code:: python

    import asyncio

    loop = asyncio.new_event_loop()

    def run_coro(coroutine, loop)
        return loop.run_until_complete(coroutine)

    # As an example, get images
    images = run_coro(api.search_images(limit=1))

You are now ready to read the :ref:`api-documentation` to view all the methods.
