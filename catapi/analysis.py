# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 Ephreal under the MIT License.
To view the license and requirements when distributing this software, please
view the license at https://github.com/ephreal/catapi/LICENSE.
"""


__all__ = ("Analysis", )


class Analysis():
    """
    Analysis schema according to thecatapi.com

    approved:
        - min 0
        - max 1
    image_id: string
    labels: list[]
    moderation_labels: list[]
    rejected: int
        - min 0
        - max 1
    vendor: string

    Analysis schema according to me based on information coming back from tests

    created_at: string
    image_id: string
    labels: list[dict]
    moderation_labels: list[]
    vendor: string
    """

    __slots__ = ("approved", "created_at", "image_id", "labels",
                 "moderation_labels", "rejected", "vendor")

    def __init__(self, **kwargs):
        self.approved = kwargs.pop("approved", 0)
        self.created_at = kwargs.pop("created_at", "")
        self.image_id = kwargs.pop("image_id", "")
        self.labels = kwargs.pop("labels", [])
        self.moderation_labels = kwargs.pop("moderation_labels", [])
        self.rejected = kwargs.pop("rejected", 0)
        self.vendor = kwargs.pop("vendor", "")
