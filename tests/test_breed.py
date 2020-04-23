# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 Ephreal under the MIT License.
To view the license and requirements when distributing this software, please
view the license at https://github.com/ephreal/catapi/LICENSE.
"""

from tests import async_capable
from catapi import breed


ATTRS = {"alt_names": "snark", "country_code": "UK", "id": "123",
         "name": "siamese", "origin": "orient", "temperment": "calm",
         "weight_imperial": "123", "weight_metric": "345",
         "energy_level": 2, "intelligence": 3}


class TestBreed(async_capable.AsyncTestCase):
    def setUp(self):
        pass

    def test_initialization(self):
        """
        Verifies Breed object can be created
        """
        # First verify that a simple object can be made
        sia = breed.Breed(name="siamese")
        self.assertEqual(sia.name, "siamese")

        # Now for one a little more complex
        sia = breed.Breed(**ATTRS)
        self.assertEqual(sia.intelligence, 3)

    def test_to_dict(self):
        """
        Verifies that a dict of attributes is returned properly.
        """

        sia = breed.Breed(**ATTRS)
        sia = self.run_coro(sia.to_dict())

        self.assertEqual(sia["name"], "siamese")

    def test_from_dict(self):
        """
        verifies that creating a Breed object from a dict works properly.
        Notably, this includes removing the "weight" attribute and adding in
        it's sub-attributes "weight_imperial" and "weight_metric"
        """

        ATTRS["weight"] = {"weight_imperial": "123", "weight_metric": "345", }
        sia = breed.Breed.from_dict(ATTRS)
        self.assertEqual(sia.temperment, "calm")
