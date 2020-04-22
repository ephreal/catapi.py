# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 Ephreal under the MIT License.
To view the license and requirements when distributing this software, please
view the license at https://github.com/ephreal/catapi/LICENSE.
"""

import asyncio
import json
from catapi import requests
from tests import async_capable

with open("secrets.json", "r") as f:
    API_KEY = json.loads(f.read())["api_key"]


class TestRequest(async_capable.AsyncTestCase):
    def setUp(self):
        self.loop = asyncio.new_event_loop()

    def tearDown(self):
        self.loop.close()

    def test_initialization(self):

        catapi = requests.CatApi(api_key=None)
        self.assertEqual(catapi.api_key, None)

        catapi = requests.CatApi(api_key=API_KEY)
        self.assertTrue(catapi.api_key)

    def test_breeds(self):
        """
        Verifies that breeds is searching for breeds properly
        """

        catapi = requests.CatApi(api_key=API_KEY)
        breeds = self.run_coro(catapi.breeds())
        self.assertEqual(len(breeds), 5)

        breeds = self.run_coro(catapi.breeds(limit=2))
        self.assertEqual(len(breeds), 2)

    def test_categories(self):
        """
        Verifies that categories returns the appropriate amount of categories
        """

        catapi = requests.CatApi(api_key=API_KEY)
        categories = self.run_coro(catapi.categories())
        self.assertEqual(len(categories), 7)

        categories = self.run_coro(catapi.categories(limit=2))
        self.assertEqual(len(categories), 2)

    def test_search(self):
        """
        Verifies that the search functionality works with or without all
        keywords.
        """

        # Get a single random image
        catapi = requests.CatApi(api_key=API_KEY)
        image = self.run_coro(catapi.search())
        self.assertTrue(image[0].image)

    def test_search_breeds(self):
        """
        Verifies that searching for breeds works without errors.
        """

        catapi = requests.CatApi(api_key=API_KEY)
        breed = self.run_coro(catapi.search_breeds("siamese"))
        self.assertEqual(len(breed), 1)
        breed = breed[0]
        self.assertEqual(breed.breed.name, "Siamese")
