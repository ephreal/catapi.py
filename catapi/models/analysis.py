# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 Ephreal under the MIT License.
To view the license and requirements when distributing this software, please
view the license at https://github.com/ephreal/catapi/LICENSE.
"""


from .abc.model_abc import Model

__all__ = ("Analysis", )


class Analysis(Model):
    """Analysis schema according to thecatapi.com

    Attributes
    ----------

    approved: :class:`int`
        Whether or not the image was approved. 1 == True, 0 == False

    created_at: :class:`string`
        Datatime string indicating when the analysis was performed

    image_id: :class:`string`
        String id of the image this analysis is from

    labels: [:class:`dict`]
        Dicts containing information about analysis labels

    moderation_labels: [:class:`dict`]
        Dicts containing reasons the image may be under moderation

    rejected: :class:`int`
        Whether or not the image was rejected. 1 == True, 0 == false

    vendor: :class:`string`
        The vendor performing the analysis
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
