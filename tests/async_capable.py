# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 Ephreal under the MIT License.
To view the license and requirements when distributing this software, please
view the license at https://github.com/ephreal/catapi/LICENSE.
"""

import asyncio
import unittest


class AsyncTestCase(unittest.TestCase):

    @classmethod
    def run_coro(self, coroutine):
        """
        runs a coroutine until completion and returns the result
        """

        loop = asyncio.get_event_loop()
        return loop.run_until_complete(coroutine)
