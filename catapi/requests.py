# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 Ephreal under the MIT License.
To view the license and requirements when distributing this software, please
view the license at https://github.com/ephreal/catapi/LICENSE.
"""


import aiohttp
from .response import Response

__all__ = ("CatApi",)

# url for v1.1 of TheCatApi
API_VERSION = "v1"
BASE_URL = f"https://api.thecatapi.com/{API_VERSION}"


class CatApi():
    """
    Handles all requesting and returning of data from the cat api.
    You can get an api key for the api here: https://thecatapi.com/signup
    Signing up for the api is free and only takes a few seconds.

    api-key: string
             authentication for thecatapi
    """

    __slots__ = ("api_key",)

    def __init__(self, **kwargs):
        self.api_key = kwargs.pop("api_key", None)

    async def breeds(self, page=0, limit=5, attach_breed=None):
        """
        Requests breeds from thecatapi. Without any parameters passed in,
        requests the first 5 breeds from the API.

        attach_breed: int (1 or 0)
            ?? I have no idea what this does yet. There's no description for it
            on thecatapi.com
        page: int
            Which page to return results from
        limit: int
            How many results will make up a page.
        """

        url = f"{BASE_URL}/breeds?limit={limit}&page={page}" \
              f"attach_breed={attach_breed}"

        breeds = await self.api_session(url)
        responses = [Response(breed=breed) for breed in breeds]
        [await response.post_initialization() for response in responses]
        return responses

    async def categories(self, limit=7, page=0):
        """
        Gets the categories available through the api. By default, returns the
        current total of 7 categories.
        """

        url = f"{BASE_URL}/categories?limit={limit}&page={page}"
        categories = await self.api_session(url)
        responses = [Response(category=category) for category in categories]
        [await response.post_initialization() for response in responses]
        return responses

    async def search(self, **kwargs):
        """
        This search method may take up to 8 args.By default, this returns a
        single random cat image.

        breed_id: string (use CatApi.breeds() to find available breeds)
        category_ids: list[int], (I don't know how to use this yet)
        format: string ("json" or "src")
        limit: int (min: 1, max: 100)
        mime_types: list[string] (I am not sure what values this takes)
        order: string ("ASC", "DESC", "RANDOM")
        size: string ("full", "med", "small", "thumbnail")
        page: int (min: 0)
        """

        breed_id = kwargs.pop("breed_id", "")
        category_ids = kwargs.pop("category_ids", "")
        format = kwargs.pop("format", "")
        limit = kwargs.pop("limit", 1)
        mime_types = kwargs.pop("mime_types", "")
        order = kwargs.pop("order", "RANDOM")
        size = kwargs.pop("size", "med")
        page = kwargs.pop("page", 0)

        url = f'{BASE_URL}/images/search?breed_id={breed_id}&category_ids=' \
              f'{category_ids}&format={format}&limit={limit}&mime_types=' \
              f'{mime_types}&order={order}&size={size}&page={page}'

        images = await self.api_session(url)
        responses = []

        for image in images:
            breed = None
            categories = None
            try:
                breed = image.pop("breeds")
            except KeyError:
                # Breeds missing, continue on
                pass

            try:
                categories = image.pop("categories")
            except KeyError:
                # Does not have categories, continue on
                pass

            responses.append(Response(breed=breed, categories=categories,
                                      image=image))

        [await response.post_initialization() for response in responses]
        return responses

    async def search_breeds(self, breed=None):
        """
        Requests breeds from the cat API. If breed_id, page, and limit are
        None, it requests the first 5 breeds by default.

        breed: string
            A string with part or all of the cat breed name.
        """

        url = f"{BASE_URL}/breeds/search?q={breed}"
        breeds = await self.api_session(url)
        responses = [Response(breed=breed) for breed in breeds]
        [await response.post_initialization() for response in responses]
        return responses

    async def api_session(self, url):
        """
        Starts an aiohttp client session and returns the result of fetching
        data. If api_key is not set, this will raise an error.
        """
        if not self.api_key:
            raise AttributeError("You must set api_key to use the API")

        headers = {"x-api-key": self.api_key}

        async with aiohttp.ClientSession() as session:
            return await self.fetch(session, url, headers)

    @classmethod
    async def fetch(self, session, url, headers):
        async with session.get(url, headers=headers) as html:
            html = await html.json()

        return html


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", "--k", help="catapi API key")
