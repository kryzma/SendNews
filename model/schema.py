from typing import Optional
import hashlib


class Post:
    """
    A class to represent a single news post
    """
    title: str
    description: str
    source: str
    link: str
    rating: int
    hash_id: str

    def __init__(self, title: str, description: str, source: str, link: str, rating: int = -1, hash_id: str = None):
        self.title = title.strip()
        self.description = description.strip()
        self.source = source.strip()
        self.link = link.strip()
        self.rating = rating
        self.hash_id = self.__hash__() if hash_id is None else hash_id

    def __hash__(self) -> str:
        source = self.title + self.description + self.source + self.link
        return hashlib.sha256(str.encode(source)).hexdigest()

    @staticmethod
    def from_json(json_dct):
        return Post(json_dct["title"],
                    json_dct["description"],
                    json_dct["source"],
                    json_dct["link"],
                    json_dct["rating"],
                    json_dct["_id"])
