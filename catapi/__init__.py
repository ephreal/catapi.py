# -*- coding: utf-8 -*-

"""
TheCatApi API wrapper

:copyright: (c) 2020 Ephreal
:license: MIT, see LICENSE for more details

"""

__title__ = 'catapi'
__author__ = 'Ephreal'
__license__ = 'MIT'
__copyright__ = 'Copyright 2020 Ephreal'
__version__ = '0.4.0'


from collections import namedtuple

from .catapi import CatApi


VersionInfo = namedtuple('VersionInfo',
                         'major minor micro releaselevel serial')

version_info = VersionInfo(major=0, minor=4, micro=0, releaselevel="alpha",
                           serial=0)
