# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 Ephreal under the MIT License.
To view the license and requirements when distributing this software, please
view the license at https://github.com/ephreal/catapi/LICENSE.
"""


__all__ = ('Breed',)


class Breed():
    """
    TheCatApi schema for a breed is:
        alt_names: string
        country_code: string
        id: string
        life_span: string
        name: string
        origin: string
        temperment: string
        weight_imperial: string
        weight_metric: string
        wikipedia_url: string

        adaptability: int, (min 1, max 5)
        affection_level: int, (min 1, max 5)
        child_friendly: int, (min 1, max 5)
        dog_friendly: int, (min 1, max 5)
        energy_level: int, (min 1, max 5)
        experimental: int, (min 0, max 1)
        grooming: int, (min 1, max 5)
        hairless: int, (min 0, max 1)
        health_issues: int, (min 1, max 5)
        hypoallergenic: int, (min 0, max 1)
        intelligence: int, (min 1, max 5)
        natural: int, (min 0, max 1)
        shedding_level: int, (min 1, max 5)
        rare: int, (min 0, max 1)
        rex: int, (min 0, max 1)
        short_legs: int, (min 0, max 1)
        social_needs: int, (min 1, max 5)
        stranger_friendly: int, (min 1, max 5)
        suppress_tail: int, (min 0, max 1)
        vocalisation: int, (min 1, max 5)
    """

    __slots__ = ('alt_names', 'country_code', 'id', 'life_span',
                 'name', 'origin', 'temperment', 'weight_imperial',
                 'weight_metric', 'wikipedia_url',
                 'adaptability', 'affection_level', 'child_friendly',
                 'dog_friendly', 'energy_level', 'experimental',
                 'grooming', 'hairless', 'health_issues', 'hypoallergenic',
                 'intelligence', 'natural', 'shedding_level', 'rare', 'rex',
                 'short_legs', 'social_needs', 'stranger_friendly',
                 'suppress_tail', 'vocalisation')

    def __init__(self, **kwargs):
        self.alt_names = kwargs.pop('alt_names', None)
        self.country_code = kwargs.pop('country_code', None)
        self.id = kwargs.pop('id', None)
        self.life_span = kwargs.pop('life_span', None)
        self.name = kwargs.pop('name', None)
        self.origin = kwargs.pop('origin', None)
        self.temperment = kwargs.pop('temperment', None)
        self.weight_imperial = kwargs.pop('weight_imperial', None)
        self.weight_metric = kwargs.pop('weight_metric', None)
        self.wikipedia_url = kwargs.pop('wikipedia_url', None)
        self.adaptability = kwargs.pop('adaptability', 'None')
        self.affection_level = kwargs.pop('affection_level', None)
        self.child_friendly = kwargs.pop('child_friendly', None)
        self.dog_friendly = kwargs.pop('dog_friendly', None)
        self.energy_level = kwargs.pop('energy_level', None)
        self.experimental = kwargs.pop('experimental', None)
        self.grooming = kwargs.pop('grooming', None)
        self.hairless = kwargs.pop('hairless', None)
        self.health_issues = kwargs.pop('health_issues', None)
        self.hypoallergenic = kwargs.pop('hypoallergenic', None)
        self.intelligence = kwargs.pop('intelligence', None)
        self.natural = kwargs.pop('natural', None)
        self.shedding_level = kwargs.pop('shedding_level', None)
        self.rare = kwargs.pop('rare', None)
        self.rex = kwargs.pop('rex', None)
        self.short_legs = kwargs.pop('short_legs', None)
        self.social_needs = kwargs.pop('social_needs', None)
        self.stranger_friendly = kwargs.pop('stranger_friendly', None)
        self.suppress_tail = kwargs.pop('suppress_tail', None)
        self.vocalisation = kwargs.pop('vocalisation', None)

    async def to_dict(self):
        breed = {}
        for attribute in self.__slots__:
            value = getattr(self, attribute, None)
            if value is None:
                continue

            breed[attribute] = value

        return breed

    @classmethod
    async def from_dict(self, breed_json):
        """
        Returns a Breed object created with the breed_json data.

        breed_json: dict
        """

        try:
            weight = breed_json.pop('weight')
            breed_json['weight_imperial'] = weight['weight_imperial']
            breed_json['weight_metric'] = weight['weight_metric']
        except KeyError:
            pass

        return Breed(**breed_json)
