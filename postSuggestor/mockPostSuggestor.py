from typing import List
from random import randrange

import postSuggestor.postSuggestor as postSuggestor
from model import schema


class MockPostsSuggestor(postSuggestor.PostsSuggestor):
    def get_suggested_post(self, posts: List[schema.Post]) -> schema.Post | None:
        if len(posts) == 0:
            return None
        random_number = randrange(len(posts))
        return posts[random_number]

    def send_suggestion_result(self, post):
        pass
