# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 Ephreal under the MIT License.
To view the license and requirements when distributing this software, please
view the license at https://github.com/ephreal/catapi/LICENSE.
"""

from .abc.model_abc import Model
from .breed import Breed
from .category import Category


__all__ = ('Image',)


class Image(Model):
    """
    Image schema from thecatapi. Note: This includes some which appear to be
    undocumented. It's currently unknown if these undocumeted items are newly
    added in, or if they were simply overlooked.

    id: string
    url: string
    sub_id: string
    created_at: datetime
    original_filename: string
    width: int
    height: int
    breed: Breed()
    categories: list[Category]
    """

    __slots__ = ("id", "url", "sub_id", "created_at", "original_filename",
                 "width", "height", 'breed', 'categories')

    def __init__(self, **kwargs):
        self.breed = kwargs.pop('breed', None)
        self.categories = kwargs.pop('categories', None)
        self.id = kwargs.pop("id", None)
        self.url = kwargs.pop("url", None)
        self.sub_id = kwargs.pop("sub_id", None)
        self.created_at = kwargs.pop("created_at", None)
        self.original_filename = kwargs.pop("original_filename", None)
        self.width = kwargs.pop("width", None)
        self.height = kwargs.pop("height", None)

        if self.categories:
            self.categories = [Category(**category) for category in self.categories]

        if self.breed:
            self.breed = Breed.from_dict(self.breed)
