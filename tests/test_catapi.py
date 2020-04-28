# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 Ephreal under the MIT License.
To view the license and requirements when distributing this software, please
view the license at https://github.com/ephreal/catapi/LICENSE.
"""

import asyncio
import json
from catapi import catapi
from tests import async_capable

with open("secrets.json", "r") as f:
    API_KEY = json.loads(f.read())["api_key"]


class TestRequest(async_capable.AsyncTestCase):
    """
    Note: both vote commands have no testing happening as currently,
          I have no votes to test on.
    """
    def setUp(self):
        self.api = catapi.CatApi(api_key=API_KEY)
        self.loop = asyncio.new_event_loop()

    def tearDown(self):
        for image in self.run_coro(self.api.get_uploads(limit=100)):
            self.run_coro(self.api.delete_image(image.id))

        for favorite in self.run_coro(self.api.get_favorites(limit=100)):
            self.run_coro(self.api.delete_favorite(favorite.id))

        for vote in self.run_coro(self.api.get_votes(limit=100)):
            self.run_coro(self.api.delete_vote(vote.id))

        self.loop.close()

    def test_initialization(self):

        api = catapi.CatApi(api_key=None)
        self.assertEqual(api.api_key, None)

        api = catapi.CatApi(api_key=API_KEY)
        self.assertTrue(api.api_key)

    def test_analysis(self):
        """
        Verifies that image analyses are returned properly.
        """

        analysis_id = "e49"
        analysis = self.run_coro(self.api.get_analysis(analysis_id))
        self.assertTrue(analysis.vendor)
        self.assertTrue(analysis.labels)

    def test_get_breeds(self):
        """
        Verifies that breeds is searching for breeds properly
        """

        api = catapi.CatApi(api_key=API_KEY)
        breeds = self.run_coro(api.get_breeds())
        self.assertEqual(len(breeds), 5)

        breeds = self.run_coro(api.get_breeds(limit=2))
        self.assertEqual(len(breeds), 2)

        self.assertTrue(breeds[0].name)

    def test_get_categories(self):
        """
        Verifies that categories returns the appropriate amount of categories
        """

        api = catapi.CatApi(api_key=API_KEY)
        categories = self.run_coro(api.get_categories())
        self.assertEqual(len(categories), 7)

        categories = self.run_coro(api.get_categories(limit=2))
        self.assertEqual(len(categories), 2)

    def test_delete_favorite(self):
        """
        Verifies that deleting favorites works
        """
        api = catapi.CatApi(api_key=API_KEY)
        favorite = self.run_coro(api.favorite("438", "automated test"))
        favorites = self.run_coro(api.get_favorites())
        self.assertEqual(len(favorites), 1)
        self.run_coro(api.delete_favorite(favorite))
        favorites = self.run_coro(api.get_favorites())
        self.assertEqual(len(favorites), 0)

    def test_get_favorite(self):
        """
        Verifies that get_favorite is able to get favorites properly
        """
        api = catapi.CatApi(api_key=API_KEY)
        favorite = self.run_coro(api.favorite("438", "automated test"))
        get_fav = self.run_coro(api.get_favorite(favorite))
        self.assertEqual(get_fav.id, favorite)
        self.run_coro(api.delete_favorite(favorite))

    def test_get_favorites(self):
        """
        Verifies that favorites returns a list of favorite objects
        """
        api = catapi.CatApi(api_key=API_KEY)
        favorite = self.run_coro(api.favorite("438", "automated test"))
        favorites = self.run_coro(api.get_favorites())
        self.assertEqual(len(favorites), 1)
        self.run_coro(api.delete_favorite(favorite))

    def test_get_image(self):
        """
        Ensures that image is able to return a single image
        """

        api = catapi.CatApi(api_key=API_KEY)
        image_id = "e49"
        image = self.run_coro(api.get_image(image_id))
        self.assertEqual(image.width, 500)
        self.assertEqual(image.height, 374)
        self.assertEqual(image.id, image_id)

    def test_search_images(self):
        """
        Verifies that the search functionality works with or without all
        keywords.
        """

        # Get a single random image
        api = catapi.CatApi(api_key=API_KEY)
        image = self.run_coro(api.search_images())
        self.assertTrue(image[0].url)

    def test_search_breeds(self):
        """
        Verifies that searching for breeds works without errors.
        """

        api = catapi.CatApi(api_key=API_KEY)
        breed = self.run_coro(api.search_breeds("siamese"))
        self.assertEqual(len(breed), 1)
        breed = breed[0]
        self.assertEqual(breed.name, "Siamese")

    def test_get_uploads(self):
        """
        Verifies that uploads are properly found.
        """

        api = catapi.CatApi(api_key=API_KEY)
        uploads = self.run_coro(api.get_uploads())
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

    def test_delete_vote(self):
        """
        Verifies that vote deletion returns correctly.
        """

        image_id = 'e3fZI02Ui'
        sub_id = "test vote performed by unittest"
        vote = self.run_coro(self.api.vote(image_id, 1, sub_id))
        self.run_coro(self.api.delete_vote(vote))
        self.run_coro(self.api.delete_vote(vote.id))
        votes = self.run_coro(self.api.get_votes())
        self.assertEqual(votes, [])

    def test_get_vote(self):
        """
        Verifies that getting a vote by id is functional.
        """
        image_id = 'e3fZI02Ui'
        sub_id = "test vote performed by unittest"
        vote = self.run_coro(self.api.vote(image_id, 1, sub_id))
        vote_id = self.run_coro(self.api.get_vote(vote.id))
        vote_id = vote_id.id
        self.assertEqual(vote.id, vote_id)
        self.assertEqual(vote.sub_id, "test vote performed by unittest")
        self.assertTrue(vote.created_at)
        self.assertEqual(vote.value, 1)
        self.assertEqual(vote.country_code, "US")

    def test_vote(self):
        """
        Verifies that voting, both up and down, work.
        """

        # Test upvoting first
        image_id = 'e3fZI02Ui'
        sub_id = "test vote performed by unittest"
        value = 1

        vote = self.run_coro(self.api.vote(image_id, value, sub_id))
        self.assertTrue(vote.id)

        # test downvote next
        value = 0
        vote = self.run_coro(self.api.vote(image_id, value, sub_id))
        self.assertTrue(vote.id)

    def test_get_votes(self):
        """
        Verifies that user voting works
        """
        image_id = 'e3fZI02Ui'
        sub_id = "test vote performed by unittest"
        self.run_coro(self.api.vote(image_id, 1, sub_id))

        votes = self.run_coro(self.api.get_votes())
        self.assertTrue(votes)
