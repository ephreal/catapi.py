# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 Ephreal under the MIT License.
To view the license and requirements when distributing this software, please
view the license at https://github.com/ephreal/catapi/LICENSE.
"""

from catapi import image
from tests import async_capable


class TestImage(async_capable.AsyncTestCase):
    def setUp(self):
        pass

    def test_initialization(self):
        """
        verifies that image objects initialize without errors
        """

        test = {"id": "asdf", "url": "example.com/quux.jpg"}
        test = image.Image(**test)
        self.assertEqual(test.id, "asdf")
        self.assertEqual(test.url, "example.com/quux.jpg")

    def test_to_dict(self):
        """
        Verifies to_dict returns a dict object with the correct data
        """
        test = {"id": "asdf", "url": "example.com/quux.jpg"}
        test = image.Image(**test)
        test = self.run_coro(test.to_dict())
        self.assertEqual(test['id'], "asdf")
        self.assertEqual(test['url'], "example.com/quux.jpg")
