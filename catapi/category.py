# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 Ephreal under the MIT License.
To view the license and requirements when distributing this software, please
view the license at https://github.com/ephreal/catapi/LICENSE.
"""

__all__ = ("Category")


class Category():
    """
    TheCatApi schema for categories
    id: int
    name: string
    """

    __slots__ = ("id", "name")

    def __init__(self, **kwargs):
        self.id = kwargs.pop("id", None)
        self.name = kwargs.pop("name", None)

    async def to_dict(self):
        """
        Returns a dict with all the attributes of the category
        """

        py_dict = {}
        for attribute in self.__slots__:
            value = getattr(self, attribute, None)
            if value is None:
                continue

            py_dict[attribute] = value

        return py_dict
