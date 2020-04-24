# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 Ephreal under the MIT License.
To view the license and requirements when distributing this software, please
view the license at https://github.com/ephreal/catapi/LICENSE.
"""

from abc import ABC


class Model(ABC):
    """
    Abstract class for all database models.

    Methods provided:
        to_dict:
            - Async method that returns all items in __slots__ formatted as a
              dict
    """

    __slots__ = ()

    def __init__(self):
        pass

    async def to_dict(self):
        attributes = {}
        for attribute in self.__slots__:
            value = getattr(self, attribute, None)
            if value is None:
                continue

            attributes[attribute] = value

        return attributes
