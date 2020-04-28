# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 Ephreal under the MIT License.
To view the license and requirements when distributing this software, please
view the license at https://github.com/ephreal/catapi/LICENSE.
"""


from .abc.model_abc import Model


__all__ = ("Category")


class Category(Model):
    """
    TheCatApi schema for categories
    id: int
    name: string
    """

    __slots__ = ("id", "name")

    def __init__(self, **kwargs):
        self.id = kwargs.pop("id", None)
        self.name = kwargs.pop("name", None)
