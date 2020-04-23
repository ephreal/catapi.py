# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 Ephreal under the MIT License.
To view the license and requirements when distributing this software, please
view the license at https://github.com/ephreal/catapi/LICENSE.
"""


from catapi.vote import Vote
from tests import async_capable


class TestVote(async_capable.AsyncTestCase):
    def setUp(self):
        pass

    def test_initialization(self):
        """
        Verifies vote objects are created without errors.
        """

        vote_params = {"value": 10, "id": "asdf", "image_id": "qwer"}
        vote = Vote(**vote_params)
        self.assertEqual(vote.value, 10)
