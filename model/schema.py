import json
from typing import Optional
import hashlib

import pydantic


class Post(pydantic.BaseModel):
    """
    A class to represent a single news post
    """
    title: str
    description: str
    source: str
    link: str
    rating: int | None = None
    hash_id: str | None = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.hash_id is None:
            self.hash_id = self.__hash__()
        if self.rating is None:
            self.rating = -1

    def __hash__(self) -> str:
        source = self.title + self.description + self.source + self.link
        return hashlib.sha256(str.encode(source)).hexdigest()

    def to_json(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)