from abc import ABC, abstractmethod
from typing import List
from random import randrange

import schema
import postSuggestor


class MockPostsSuggestor(postSuggestor.PostsSuggestor):
    def get_suggested_post(self, posts: List[schema.Post]) -> schema.Post:
        random_number = randrange(len(posts))
        return posts[random_number]

    def send_suggestion_result(self, posts):
        pass
