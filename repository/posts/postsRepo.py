from abc import ABC, abstractmethod
from typing import List

from src.model import schema


class PostsRepository(ABC):
    """
    A class to represent an interface for Posts repository
    """

    @abstractmethod
    def insert_post(self, post: schema.Post):
        pass

    @abstractmethod
    def update_post_rating(self, hash: str, rating: int):
        pass

    @abstractmethod
    def get_post_by_hash(self, hash: str) -> schema.Post | None:
        pass

    @abstractmethod
    def get_unrated_posts(self) -> List[schema.Post]:
        pass

    @abstractmethod
    def get_all_posts(self) -> List[schema.Post]:
        pass

