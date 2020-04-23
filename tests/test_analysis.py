# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 Ephreal under the MIT License.
To view the license and requirements when distributing this software, please
view the license at https://github.com/ephreal/catapi/LICENSE.
"""


from catapi.analysis import Analysis
from tests import async_capable


class Testanaylsis(async_capable.AsyncTestCase):
    def setUp(self):
        pass

    def test_initialization(self):
        """
        Verifies analysis objects are created without errors.
        """

        analysis_params = {"vendor": "quux", "rejected": 0, "approved": 1}
        analysis = Analysis(**analysis_params)
        self.assertEqual(analysis.vendor, "quux")
