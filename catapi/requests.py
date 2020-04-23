# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 Ephreal under the MIT License.
To view the license and requirements when distributing this software, please
view the license at https://github.com/ephreal/catapi/LICENSE.
"""


import aiohttp
from .analysis import Analysis
from .breed import Breed
from .category import Category
from .image import Image
from .vote import Vote

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

    async def analysis(self, image_id):
        """
        Get the analysis results of an image.

        image_id: string
        """

        url = f"{BASE_URL}/images/{image_id}/analysis"
        analysis = await self.api_get_session(url)
        return Analysis(**analysis[0])

    async def breeds(self, page=0, limit=5, attach_breed=""):
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

        params = {"attach_breed": attach_breed, "limit": limit, "page": page}

        url = f"{BASE_URL}/breeds"

        breeds = await self.api_get_session(url, params)
        breeds = [Breed.from_dict(breed) for breed in breeds]
        return breeds

    async def categories(self, limit=7, page=0):
        """
        Gets the categories available through the api. By default, returns the
        current total of 7 categories.
        """

        params = {"limit": limit, "page": page}

        url = f"{BASE_URL}/categories"
        categories = await self.api_get_session(url, params)
        categories = [Category(**category) for category in categories]
        return categories

    async def image(self, image_id):
        """
        Gets a specific image by id from the api.

        image_id: string
        """

        url = f"{BASE_URL}/images/{image_id}"
        image = await self.api_get_session(url)
        return Image(**image)

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

        params = {
            'breed_id': kwargs.pop("breed_id", ""),
            'category_ids': kwargs.pop("category_ids", ""),
            'format': kwargs.pop("format", ""),
            'limit': kwargs.pop("limit", 1),
            'mime_types': kwargs.pop("mime_types", ""),
            'order': kwargs.pop("order", "RANDOM"),
            'size': kwargs.pop("size", "med"),
            'page': kwargs.pop("page", 0),
        }

        url = f'{BASE_URL}/images/search'

        images = await self.api_get_session(url, params)
        images = [Image(**image) for image in images]
        return images

    async def search_breeds(self, breed=None):
        """
        Requests breeds from the cat API. If breed is None, it requests the
        first 5 breeds by default.

        breed: string
            A string with part or all of the cat breed name.
        """

        params = {"q": breed}
        url = f"{BASE_URL}/breeds/search"
        breeds = await self.api_get_session(url, params)
        breeds = [Breed.from_dict(breed) for breed in breeds]
        return breeds

    async def upload(self, filepath, sub_id=""):
        """
        Uploads a file to thecatapi.

        filepath: string
        sub_id: string
            - Custom value you may add to be stored with the file
        """

        params = {"sub_id": sub_id}
        url = f"{BASE_URL}/images/upload"
        with open(filepath, 'rb') as data:
            success_status = await self.api_post_session(url, {"file": data},
                                                         params)
        return success_status

    async def uploads(self, **kwargs):
        """
        Allows you to get images you have uploaded to thecatapi. This accepts
        10 keyword arguments.

        breed_ids: list[string]
            - items in list must be unique
        category_ids: list[string]
            - items in list must be unique
        format: string
            - json, src
        include_favorite: int
            - min 0
            - max 1
        include_vote: int
            - min 0
            - max 1
        limit: int
            - min 1
            - max 100
        order: string
            - ASC
            - DESC
            - RANDOM
        original_filename: string
            - min length: 0
            - max length: 100
        page: int
            - min: 1
        sub_id: string
            - min length: 0
            - max length: 255
        """

        params = {
            'breed_ids': kwargs.pop('breed_ids', ''),
            'category_ids': kwargs.pop('category_ids', ''),
            'format': kwargs.pop('format', ''),
            'include_favorite': kwargs.pop('include_favorite', ''),
            'include_vote': kwargs.pop('include_vote', ''),
            'limit': kwargs.pop('limit', 1),
            'order': kwargs.pop('order', 'DESC'),
            'original_filename': kwargs.pop('original_filename', ''),
            'page': kwargs.pop('page', 1),
            'sub_id': kwargs.pop('sub_id', ''),
        }

        url = f"{BASE_URL}/images/"
        images = await self.api_get_session(url, params)
        images = [Image(**image) for image in images]
        return images

    async def get_vote(self, vote_id):
        """
        Gets a particular vote.

        vote_id: string
        """

        url = f"{BASE_URL}/votes/{vote_id}"
        vote = await self.api_get_session(url)
        return Vote(**vote)

    async def vote(self, image_id, value, sub_id):
        """
        Casts a vote on the image specified by image_id

        value == 0 is a downvote
        value == 1 is an upvote

        Note: thecatapi contridicts itself. This should return a "vote" object,
              but instead, it is a dict with success/fail status and vote id.

              In accordance with the API documentation, I return a vote object

        image_id: string
        value: int
            - min 0
            - max 1
        sub_id: string
        """

        data = {"image_id": image_id, "sub_id": sub_id, "value": value}
        url = f"{BASE_URL}/votes"
        success_status = await self.api_post_session(url, data, json=True)

        # if successful, success_status should be able to be a Vote object
        try:
            success_status = Vote(**success_status)
        except TypeError:
            # Unsuccessful at creating a vote. I will raise errors here in the
            # future. For now... pass and return the error message.
            pass

        return success_status

    async def votes(self, limit=10, page=0, sub_id=""):
        """
        Gets a list of all votes you have created. By default, with no options,
        this gets the first 10 votes on images you have cast.

        limit: int
        page: int (min 0)
        sub_id: string
        """

        params = {"limit": limit, "page": page, "sub_id": sub_id}
        url = f"{BASE_URL}/votes"
        votes = await self.api_get_session(url, params)
        votes = [Vote(**vote) for vote in votes]
        return votes

    async def api_get_session(self, url, params=None):
        """
        Starts an aiohttp client session and returns the result of fetching
        data. If api_key is not set, this will raise an error.
        """
        if not self.api_key:
            raise AttributeError("You must set api_key to use the API")

        headers = {"x-api-key": self.api_key}

        async with aiohttp.ClientSession() as session:
            return await self.fetch(session, url, headers, params)

    async def api_post_session(self, url, data, params=None, json=False):
        """
        Uploads data to the url via post.

        url: string
        data: dict{key: value}
        params: dict{}
        """

        if not self.api_key:
            raise AttributeError("You must set api_key to use the API")

        headers = {"x-api-key": self.api_key}

        async with aiohttp.ClientSession() as session:
            return await self.post(session, url, data, headers, params, json)

    @classmethod
    async def fetch(self, session, url, headers, params=None):
        async with session.get(url, headers=headers, params=params) as html:
            html = await html.json()

        return html

    @classmethod
    async def post(self, session, url, data, headers, params=None, json=False):
        if not json:
            async with session.post(url, headers=headers, params=params,
                                    data=data) as status:
                status = await status.text()
        else:
            async with session.post(url, headers=headers, json=data) as status:
                status = await status.json()

        return status


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", "--k", help="catapi API key")
    parser.add_argument("-b", "--breed", help="Breeds")
