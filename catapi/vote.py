# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 Ephreal under the MIT License.
To view the license and requirements when distributing this software, please
view the license at https://github.com/ephreal/catapi/LICENSE.
"""

__all__ = ("Vote",)


class Vote():
    """
    Vote schema according to thecatapi.

    created_at: string
    country_code: string
    value: int (required)
    image_id: string (required)
    sub_id: string (apparently required, docs do not mention this)
    id: string
    country_code: string
    """

    __slots__ = ("image_id", "value", "sub_id", "created_at", "id",
                 "country_code", "created_at")

    def __init__(self, **kwargs):
        self.image_id = kwargs.pop('image_id', "")
        self.value = kwargs.pop('value', None)

        self.country_code = kwargs.pop("country_code", "")
        self.created_at = kwargs.pop("created_at", "")
        self.id = kwargs.pop("id", "")
        self.sub_id = kwargs.pop("sub_id", "")
