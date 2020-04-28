# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 Ephreal under the MIT License.
To view the license and requirements when distributing this software, please
view the license at https://github.com/ephreal/catapi/LICENSE.
"""

from .abc.model_abc import Model

__all__ = ("Vote",)


class Vote(Model):
    """Vote schema according to thecatapi.

    created_at: :class:`string`
        A string indicating when the vote was created

    country_code: :class:`string`
        A string indicating the country of origin for the vote

    value: Required :class:`int`
        An int indicating an upvote (1) or downvote (0)

    image_id: :class:`string (required)`
        String ID referencing the image the vote applies to

    sub_id: Required :class:`string`
        Custom information to store with the vote

    id: :class:`string`
        String id of the vote
    """

    __slots__ = ("image_id", "value", "sub_id", "created_at", "id",
                 "country_code", )

    def __init__(self, **kwargs):
        self.image_id = kwargs.pop('image_id', "")
        self.value = kwargs.pop('value', None)

        self.country_code = kwargs.pop("country_code", "")
        self.created_at = kwargs.pop("created_at", "")
        self.id = kwargs.pop("id", "")
        self.sub_id = kwargs.pop("sub_id", "")
