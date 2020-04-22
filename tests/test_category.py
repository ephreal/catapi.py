# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 Ephreal under the MIT License.
To view the license and requirements when distributing this software, please
view the license at https://github.com/ephreal/catapi/LICENSE.
"""

from catapi import category
from tests import async_capable


class TestCategory(async_capable.AsyncTestCase):
    def setUp(self):
        pass

    def test_initialization(self):
        """
        Verifies that categories are able to be made properly.
        """
        test = {"id": 7, "name": "Sneks"}
        test = category.Category(**test)
        self.assertEqual(test.id, 7)
        self.assertEqual(test.name, "Sneks")

    def test_to_dict(self):
        """
        Verifies to_dict returns a dict object with the correct data
        """
        test = {"id": 2, "name": "Gloversade"}
        test = category.Category(**test)
        test = self.run_coro(test.to_dict())
        self.assertEqual(test['id'], 2)
        self.assertEqual(test['name'], "Gloversade")
