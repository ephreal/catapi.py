# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 Ephreal under the MIT License.
To view the license and requirements when distributing this software, please
view the license at https://github.com/ephreal/catapi/LICENSE.
"""

__all__ = ('Image',)


class Image():
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
    """

    __slots__ = ("id", "url", "sub_id", "created_at", "original_filename",
                 "width", "height")

    def __init__(self, **kwargs):
        self.id = kwargs.pop("id", None)
        self.url = kwargs.pop("url", None)
        self.sub_id = kwargs.pop("sub_id", None)
        self.created_at = kwargs.pop("created_at", None)
        self.original_filename = kwargs.pop("original_filename", None)
        self.width = kwargs.pop("width", None)
        self.height = kwargs.pop("height", None)

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
