# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 Ephreal under the MIT License.
To view the license and requirements when distributing this software, please
view the license at https://github.com/ephreal/catapi/LICENSE.
"""

from .breed import Breed
from .category import Category
from .image import Image


__all__ = ("Response")


class Response():
    """
    Response is used to provide a complete picture of the data. Sometimes the
    API returns additional data along with images. The response class ensures
    that all data is accounted for.
    """

    __slots__ = ("breed", "image", "categories")

    def __init__(self, **kwargs):
        self.breed = kwargs.pop("breed", None)
        self.image = kwargs.pop("image", None)
        self.categories = kwargs.pop("categories", None)

    async def post_initialization(self):
        """
        Initializes the variables to the correct objects. Necessary for asyncio
        as using await is invalid in a constructor.
        """

        if self.breed:
            self.breed = await Breed.from_dict(self.breed)

        if self.image:
            self.image = Image(**self.image)

        if self.categories:
            self.categories = Category(**self.categories)
