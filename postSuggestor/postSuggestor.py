from abc import ABC, abstractmethod
from typing import List

from model import schema


class PostsSuggestor(ABC):
    """
    A class to represent an interface for Machine learning model
    """

    @abstractmethod
    def get_suggested_post(self, posts: List[schema.Post]) -> schema.Post:
        """
        returns suggested post from unseen posts
        """
        pass

    @abstractmethod
    def send_suggestion_result(self, posts):
        """
        retrieves suggestion result, used for improving suggestions
        """
        pass




