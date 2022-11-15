from typing import List

import schema
import exceptions
from repository.posts.postsRepo import PostsRepository


class MockPostsRepository(PostsRepository):
    posts: List[schema.Post]

    def __init__(self):
        self.posts: List[schema.Post] = []

    def insert_post(self, post: schema.Post):
        self.posts.append(post)

    def update_post_score(self, hash: str, score: int):
        for idx, post in enumerate(self.posts):
            if post.hash_id == hash:
                self.posts[idx].hash_id = hash
                break

    def get_post_by_hash(self, hash: str) -> schema.Post:
        for post in self.posts:
            if post.hash == hash:
                return post

        raise exceptions.ResourceNotFoundException("Could not find post with hash = ", hash)

    def get_unrated_posts(self) -> List[schema.Post]:
        result: List[schema.Post] = []
        for post in self.posts:
            if post.rating is None:
                result.append(post)

        return result

    def get_all_posts(self) -> List[schema.Post]:
        return self.posts
