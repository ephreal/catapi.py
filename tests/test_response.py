# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 Ephreal under the MIT License.
To view the license and requirements when distributing this software, please
view the license at https://github.com/ephreal/catapi/LICENSE.
"""

from catapi import response
from tests import async_capable


class TestResponse(async_capable.AsyncTestCase):
    def setUp(self):
        pass

    def test_initialization(self):
        """
        Verifies that response objects can be made without errors
        """

        breed = {"name": "siamese", "id": "asdf"}
        resp = response.Response(breed=breed)
        self.run_coro(resp.post_initialization())

        self.assertEqual(resp.breed.name, "siamese")
