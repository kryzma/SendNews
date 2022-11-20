from abc import ABC, abstractmethod
from typing import List

from ..model.schema import Post


class PostsSuggestor(ABC):
    """
    A class to represent an interface for Machine learning model
    """

    @abstractmethod
    def get_suggested_post(self, posts: List[Post]) -> Post | None:
        """
        returns suggested post from unseen posts
        """
        pass

    @abstractmethod
    def send_suggestion_result(self, post):
        """
        retrieves suggestion result, used for improving suggestions
        """
        pass




