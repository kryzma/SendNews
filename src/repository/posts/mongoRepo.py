from typing import List

from ...model.schema import Post

from .postsRepo import PostsRepository

from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection


class MongoPostsRepository(PostsRepository):

    def __init__(self):
        with open("secrets", "r") as f:
            con_str = f.read()
        self.mongo_client: MongoClient = MongoClient(con_str)
        db: Database = self.mongo_client["SendNews"]
        self.posts_collection: Collection = db["Posts"]

    def insert_post(self, post: Post):
        post = \
            {"_id": post.hash_id,
             "title": post.title,
             "description": post.description,
             "link": post.link,
             "rating": post.rating,
             "source": post.source
             }
        self.posts_collection.insert_one(post)

    def update_post_rating(self, hash: str, rating: int):
        filtr: dict = {"_id": hash}
        update: dict = {"$set": {"rating": rating}}
        self.posts_collection.update_one(filtr, update)

    def get_post_by_hash(self, hash: str) -> Post | None:
        result: List[dict] = list(self.posts_collection.find({"_id": hash}))
        if len(result) == 0:
            return None
        post: Post = Post(**result[0])
        return post

    def get_unrated_posts(self) -> List[Post]:
        posts: List[Post] = []
        results: List[dict] = list(self.posts_collection.find({"rating": -1}))
        for result in results:
            posts.append(Post(**result))
        return posts

    def get_all_posts(self) -> List[Post]:
        posts: List[Post] = []
        results: List[dict] = list(self.posts_collection.find({}))
        for result in results:
            new_post: Post = Post(**result)
            posts.append(new_post)
        return posts

    def __del__(self):
        self.mongo_client.close()
