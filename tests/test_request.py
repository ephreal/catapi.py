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
    """
    Note: both vote commands have no testing happening as currently,
          I have no votes to test on.
    """
    def setUp(self):
        self.loop = asyncio.new_event_loop()

    def tearDown(self):
        self.loop.close()

    def test_initialization(self):

        catapi = requests.CatApi(api_key=None)
        self.assertEqual(catapi.api_key, None)

        catapi = requests.CatApi(api_key=API_KEY)
        self.assertTrue(catapi.api_key)

    def test_analysis(self):
        """
        Verifies that image analyses are returned properly.
        """

        id = "e49"
        catapi = requests.CatApi(api_key=API_KEY)
        analysis = self.run_coro(catapi.analysis(id))
        self.assertTrue(analysis.vendor)
        self.assertTrue(analysis.labels)

    def test_breeds(self):
        """
        Verifies that breeds is searching for breeds properly
        """

        catapi = requests.CatApi(api_key=API_KEY)
        breeds = self.run_coro(catapi.breeds())
        self.assertEqual(len(breeds), 5)

        breeds = self.run_coro(catapi.breeds(limit=2))
        self.assertEqual(len(breeds), 2)

        self.assertTrue(breeds[0].name)

    def test_categories(self):
        """
        Verifies that categories returns the appropriate amount of categories
        """

        catapi = requests.CatApi(api_key=API_KEY)
        categories = self.run_coro(catapi.categories())
        self.assertEqual(len(categories), 7)

        categories = self.run_coro(catapi.categories(limit=2))
        self.assertEqual(len(categories), 2)

    def test_image(self):
        """
        Ensures that image is able to return a single image
        """

        catapi = requests.CatApi(api_key=API_KEY)
        image_id = "e49"
        image = self.run_coro(catapi.image(image_id))
        self.assertEqual(image.width, 500)
        self.assertEqual(image.height, 374)
        self.assertEqual(image.id, image_id)

    def test_search(self):
        """
        Verifies that the search functionality works with or without all
        keywords.
        """

        # Get a single random image
        catapi = requests.CatApi(api_key=API_KEY)
        image = self.run_coro(catapi.search())
        self.assertTrue(image[0].url)

    def test_search_breeds(self):
        """
        Verifies that searching for breeds works without errors.
        """

        catapi = requests.CatApi(api_key=API_KEY)
        breed = self.run_coro(catapi.search_breeds("siamese"))
        self.assertEqual(len(breed), 1)
        breed = breed[0]
        self.assertEqual(breed.name, "Siamese")

    def test_uploads(self):
        """
        Verifies that uploads are properly found.
        """

        catapi = requests.CatApi(api_key=API_KEY)
        uploads = self.run_coro(catapi.uploads())
        self.assertEqual(len(uploads), 1)
        upload = uploads[0]

        self.assertEqual(upload.breed, None)
        self.assertEqual(upload.id, 'e3fZI02Ui')
        # I'm not sure if the url will change from time to time
        self.assertTrue(upload.url)
        self.assertEqual(upload.width, 640)
        self.assertEqual(upload.height, 480)
        self.assertEqual(upload.sub_id, None)
        self.assertEqual(upload.created_at, '2020-04-23T19:27:59.000Z')
        self.assertEqual(upload.original_filename, 'cat.jpg')

    def test_get_vote(self):
        """
        Verifies that getting a vote by id is functional.
        """

        catapi = requests.CatApi(api_key=API_KEY)

        vote_id = self.run_coro(catapi.votes(limit=1, page=0))[0].id
        vote = self.run_coro(catapi.get_vote(vote_id))
        self.assertEqual(vote.id, vote_id)
        # the user_id seems to be on and off from time to time
        # self.assertEqual(vote.user_id, "u95bfu")
        self.assertEqual(vote.sub_id, "first!")
        self.assertTrue(vote.created_at)
        self.assertEqual(vote.value, 1)
        self.assertEqual(vote.country_code, "US")

    def test_vote(self):
        """
        Verifies that voting, both up and down, work.
        """

        catapi = requests.CatApi(api_key=API_KEY)

        # Test upvoting first
        image_id = 'e3fZI02Ui'
        sub_id = "test vote performed by unittest"
        value = 1

        vote = self.run_coro(catapi.vote(image_id, value, sub_id))
        self.assertTrue(vote.id)

        # test downvote next
        value = 0
        vote = self.run_coro(catapi.vote(image_id, value, sub_id))
        self.assertTrue(vote.id)

    def test_votes(self):
        """
        Verifies that user voting works
        """

        catapi = requests.CatApi(api_key=API_KEY)
        votes = self.run_coro(catapi.votes())
        self.assertTrue(votes)
