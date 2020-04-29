# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 Ephreal under the MIT License.
To view the license and requirements when distributing this software, please
view the license at https://github.com/ephreal/catapi/LICENSE.
"""


import aiohttp
from .models.analysis import Analysis
from .models.breed import Breed
from .models.category import Category
from .models.favorite import Favorite
from .models.image import Image
from .models.vote import Vote

__all__ = ("CatApi",)

# url for v1.1 of TheCatApi
API_VERSION = "v1"
BASE_URL = f"https://api.thecatapi.com/{API_VERSION}"


class CatApi():
    """Handles all requesting and returning of data from the cat api.
    You can get an api key at https://thecatapi.com/signup .

    Signing up for the api is free and only takes a few seconds.

    Attributes
    -----------

    api_key: :class:`int`
        authentication key for thecatapi.com
    """

    __slots__ = ("api_key",)

    def __init__(self, **kwargs):
        self.api_key = kwargs.pop("api_key", None)

    async def get_analysis(self, image_id):
        """Get the analysis results of an image.

        image_id: :class:`string`
        """

        url = f"{BASE_URL}/images/{image_id}/analysis"
        analysis = await self.api_get_session(url)
        return Analysis(**analysis[0])

    async def get_breeds(self, page=0, limit=5, attach_breed=""):
        """Requests breeds from thecatapi. Without any parameters passed in,
        requests the first 5 breeds from the API.

        Parameters
        -----------

        attach_breed: :class:`int` (1 or 0)
            The usage of this is undocumented in the api documentation.

        page: :class:`int`
            Which page to return results from

        limit: :class:`int`
            How many results will make up a page.
        """

        params = {"attach_breed": attach_breed, "limit": limit, "page": page}

        url = f"{BASE_URL}/breeds"

        breeds = await self.api_get_session(url, params)
        breeds = [Breed.from_dict(breed) for breed in breeds]
        return breeds

    async def get_categories(self, limit=7, page=0):
        """Gets the categories available through the api. By default, returns
        the current total of 7 categories.

        Parameters
        ----------

        page: :class:`int`
            Which page to return results from

        limit: :class:`int`
            How many results will make up a page.
        """

        params = {"limit": limit, "page": page}

        url = f"{BASE_URL}/categories"
        categories = await self.api_get_session(url, params)
        categories = [Category(**category) for category in categories]
        return categories

    async def delete_favorite(self, favorite_id):
        """Removes an item from your favorites

        Also mapped to CatApi.delete_favourite()

        Parameters
        ----------

        favorite_id: :class:`string`
            ID of the image to delete a favorite from
        """

        url = f"{BASE_URL}/favourites/{favorite_id}"
        message = await self.api_delete_session(url)
        return message

    async def delete_favourite(self, favourite_id):
        """Removes an item from your favourites

        Also mapped to CatApi.delete_favorite()

        Parameters
        ----------

        favourite_id: :class:`string`
            ID of the image to delete a favourite from
        """

        return await self.delete_favorite(favourite_id)

    async def favorite(self, image_id, sub_id):
        """Favorite an image.

        Also mapped to CatApi.favourite()

        Parameters
        -----------

        image_id: :class:`string`
            ID of the image to favorite

        sub_id: :class:`string`
            Custom content to add when favoriting the image

            Note: testing shows sub_id is required although thecatapi says not
        """

        data = {"image_id": image_id, "sub_id": sub_id}
        url = f"{BASE_URL}/favourites"
        message = await self.api_post_session(url, data, json=True)
        if message["message"] == "SUCCESS":
            return message["id"]

        return message

    async def favourite(self, image_id, sub_id):
        """Favourite an image.

        Also mapped to CatApi.favorite()

        Parameters
        -----------

        image_id: :class:`string`
            ID of the image to favorite

        sub_id: :class:`string`
            Custom content to add when favouriting the image

            Note: testing shows sub_id is required although thecatapi says not
        """

        return self.favorite(image_id, sub_id)

    async def get_favorites(self, limit=100, page=0, sub_id=""):
        """Gets all of your favorites.

        Also mapped to CatApi.favourites()

        Parameters
        ----------

        limit: :class:`int`
            Amount of items per page

        page: :class:`int`
            Which page to access

        sub_id: :class:`string`
            Custom content placed when favoriting the image
        """

        params = {"limit": limit, "page": page, "sub_id": sub_id}
        url = f"{BASE_URL}/favourites"

        favorites = await self.api_get_session(url, params)
        favorites = [Favorite(**favorite) for favorite in favorites]
        return favorites

    async def get_favourites(self, limit=100, page=0, sub_id=None):
        """Gets all of your favourites.

        Also mapped to CatApi.favorites()

        Parameters
        ----------

        limit: :class:`int`
            Amount of items per page

        page: :class:`int`
            Which page to access

        sub_id: :class:`string`
            Custom content placed when favouriting the image
        """
        return await self.favorites(limit, page, sub_id)

    async def get_favorite(self, favorite_id):
        """Get a favorite specified by favorite id

        Also mapped to CatApi.get_favourite()

        Parameters
        ----------

        favorite_id: :class:`string`
        """

        url = f"{BASE_URL}/favourites/{favorite_id}"
        favorite = await self.api_get_session(url)
        favorite = Favorite(**favorite)
        return favorite

    async def get_favourite(self, favourite_id):
        """Get a favourite specified by favourite id

        Also mapped to CatApi.get_favorite()

        Parameters
        ----------

        favourite_id: :class:`string`
        """

        return self.get_favorite(favourite_id)

    async def delete_image(self, image_id):
        """Deletes an image specified by the image_id

        Parameters
        ----------

        image_id: :class:`string`
            ID of the image to delete
        """

        url = f"{BASE_URL}/images/{image_id}"
        message = await self.api_delete_session(url)
        return message

    async def get_image(self, image_id):
        """Gets a specific image by id from the api.

        Parameters
        ----------

        image_id: :class:`string`
            ID of the image to get
        """

        url = f"{BASE_URL}/images/{image_id}"
        image = await self.api_get_session(url)
        return Image(**image)

    async def search_images(self, **kwargs):
        """search_images may take up to 8 args. By default, this returns a
        single random cat image.

        Parameters
        ----------

        breed_id: :class:`string`
            Breed id to narrow down the search with. Find breeds with
            CatApi.get_breeds()

        category_ids: [:class:`string`]
            Filter based on category id. Currently does not appear to work.

        format: :class:`string`
            May be "json" or "src"

        limit: :class:`int`
            May be in the range of 1-100, inclusive

        mime_types: [:class:`string`]
            A list of strings. Values this takes are currently unknown

        order: :class:`string`
            May be "ASC", "DESC", or "RANDOM"

        size: :class:`string`
            May be "full", "med", "small", or "thumbnail"

        page: class`int`
            Which page to pull images from. Minimum value of 0
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
        """Requests breeds from the cat API. If breed is None, it requests all
        breeds by default.

        Parameters
        ----------

        breed: :class:`string`
            A string with part or all of the cat breed name.
        """

        params = {"q": breed}
        url = f"{BASE_URL}/breeds/search"
        breeds = await self.api_get_session(url, params)
        breeds = [Breed.from_dict(breed) for breed in breeds]
        return breeds

    async def upload(self, filepath, sub_id=""):
        """Uploads a file to thecatapi.com

        Parameters
        ----------

        filepath: :class:`string`
            Path to the jpg, png, gif, etc to upload

        sub_id: :class:`string`
            Custom value you may add to be stored with the file
        """

        params = {"sub_id": sub_id}
        url = f"{BASE_URL}/images/upload"
        with open(filepath, 'rb') as data:
            success_status = await self.api_post_session(url, {"file": data},
                                                         params)
        return success_status

    async def get_uploads(self, **kwargs):
        """Allows you to get images you have uploaded to thecatapi. Can accept
        up to 10 keyword arguments.

        Parameters
        ----------

        breed_ids: [:class:`int`]
            List of unique breed_id strings

        category_ids: [:class:`string`]
            List of unique category_id strings

        format: :class:`string`
            May be "json" or "src"

        include_favorite: :class:`int`
            May be 0 or 1

        include_vote: :class:`int`
            May be 0 or 1

        limit: :class:`int`
            May be between 1 and 100, inclusive

        order: :class:`string`
            May be "ASC", "DESC", or "RANDOM"

        original_filename: class:`string`
            get uploads that originally had this name. Length must be between
            0 and 100 characters, inclusive.

        page: class:`int`
            Which page to get results from. Minimum value of 1

        sub_id: :class:`string`
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

    async def delete_vote(self, vote_id):
        """Deletes a particular vote.

        Parameters
        ----------

        vote_id: :class:`string`
            The string id of the vote to delete
        """

        url = f"{BASE_URL}/votes/{vote_id}"
        message = await self.api_delete_session(url)
        return message

    async def get_vote(self, vote_id):
        """Gets a particular vote.

        Parameters
        ----------

        vote_id: :class:`string`
            The string id of the vote to get
        """

        url = f"{BASE_URL}/votes/{vote_id}"
        vote = await self.api_get_session(url)
        return Vote(**vote)

    async def vote(self, image_id, value, sub_id):
        """
        Casts a vote on the image specified by image_id

        Parameters
        ----------

        image_id: :class:`string`
            String ID of the image to vote on

        value: :class:`int`
            Upvote (1) or downvote (0)

        sub_id: :class:`string`
            Custom message to store along with the vote
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

    async def get_votes(self, limit=100, page=0, sub_id=""):
        """Gets a list of all votes you have created. By default, with no
        options, this gets the first 100 votes on images you have cast.

        Parameters
        ----------

        limit: :class:`int`
            How many votes to have per page

        page: :class:`int`
            The page number to get the votes from. Minimum 0

        sub_id: :class:`string`
            Custom string stored with votes
        """

        params = {"limit": limit, "page": page, "sub_id": sub_id}
        url = f"{BASE_URL}/votes"
        votes = await self.api_get_session(url, params)
        votes = [Vote(**vote) for vote in votes]
        return votes

    async def api_delete_session(self, url, params=None):
        """Starts an aiohttp session to send a delete request"""

        if not self.api_key:
            raise AttributeError("You must set api_key to use the API")

        headers = {"x-api-key": self.api_key}

        async with aiohttp.ClientSession() as session:
            return await self.delete(session, url, headers, params)

    async def api_get_session(self, url, params=None):
        """Starts an aiohttp client session and returns the result of fetching
        data.

        If api_key is not set, this will raise an error.
        """
        if not self.api_key:
            raise AttributeError("You must set api_key to use the API")

        headers = {"x-api-key": self.api_key}

        async with aiohttp.ClientSession() as session:
            return await self.fetch(session, url, headers, params)

    async def api_post_session(self, url, data, params=None, json=False):
        """Uploads data to the url via post.

        Parameters
        ----------

        url: :class:`string`
            Url to post data to

        data: :class:`dict`
            Dictionary of key/value pairs to post

        params: :class:`dict`
            Key/Value pairs of parameters for url arguments

        json: :class:`boolean`
            Whether or not to post the data as json
        """

        if not self.api_key:
            raise AttributeError("You must set api_key to use the API")

        headers = {"x-api-key": self.api_key}

        async with aiohttp.ClientSession() as session:
            return await self.post(session, url, data, headers, params, json)

    @classmethod
    async def delete(self, session, url, headers, params):
        """Sends an http delete request to the url"""
        async with session.delete(url, headers=headers, params=params) as html:
            html = await html.text()

        return html

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
