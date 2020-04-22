# -*- coding: utf-8 -*-

"""
TheCatApi API wrapper

:copyright: (c) 2020 Ephgreal
:license: MIT, see LICENSE for more details

"""

__title__ = 'catapi'
__author__ = 'Ephreal'
__license__ = 'MIT'
__copyright__ = 'Copyright 2020 Ephreal'
__version__ = '0.0.1a'


from collections import namedtuple

from .requests import CatApi


VersionInfo = namedtuple('VersionInfo',
                         'major minor micro releaselevel serial')

version_info = VersionInfo(major=0, minor=0, micro=1, releaselevel="alpha",
                           serial=0)
