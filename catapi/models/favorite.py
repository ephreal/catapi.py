# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 Ephreal under the MIT License.
To view the license and requirements when distributing this software, please
view the license at https://github.com/ephreal/catapi/LICENSE.
"""


from .abc.model_abc import Model


__all__ = ("Favorite")


class Favorite(Model):
    """TheCatApi schema for favorites

    created_at: :class:`string`
        Datetime indicating when this favorite was created

    id: :class:`string`
        String id of this favorite

    image_id: :class:`string`
        String id of the image this favorite is for

    sub_id: :class:`string`
        Custom information stored alongside the favorite
    """

    __slots__ = ("created_at", "id", "image_id", "sub_id")

    def __init__(self, **kwargs):
        self.created_at = kwargs.pop("created_at", None)
        self.id = kwargs.pop("id", None)
        self.image_id = kwargs.pop("image_id", None)
        self.sub_id = kwargs.pop("sub_id", None)
