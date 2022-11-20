from typing import List
from random import randrange

from .postSuggestor import PostsSuggestor
from ..model.schema import Post


class MockPostsSuggestor(PostsSuggestor):
    def get_suggested_post(self, posts: List[Post]) -> Post | None:
        if len(posts) == 0:
            return None
        random_number = randrange(len(posts))
        return posts[random_number]

    def send_suggestion_result(self, post):
        pass
