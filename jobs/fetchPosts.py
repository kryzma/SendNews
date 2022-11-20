from typing import List

from src.model import schema

import src.repository.rss.rssRepo as rssRepo
import src.repository.posts.mongoRepo as mongoRepo
import src.repository.posts.postsRepo as postsRepo


def update_posts(urls: List[str]):
    """
    fetches posts and inserts ones that are not in db
    """
    mr: postsRepo.PostsRepository = mongoRepo.MongoPostsRepository()
    rr: rssRepo.RssRepo = rssRepo.RssRepoImpl()

    posts: List[schema.Post] = rr.get_posts_from_urls(urls)

    for post in posts:
        if mr.get_post_by_hash(post.hash_id) is None:
            mr.insert_post(post)
