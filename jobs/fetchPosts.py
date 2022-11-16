from typing import List

import schema
import repository.rss.rssRepo as rssRepo
import repository.posts.mongoRepo as mongoRepo


def update_posts(urls: List[str]):
    """
    fetches posts and inserts ones that are not in db
    """
    mr: mongoRepo.MongoPostsRepository = mongoRepo.MongoPostsRepository()
    rr: rssRepo.RssRepo = rssRepo.RssRepoImpl()

    posts: List[schema.Post] = rr.get_posts_from_urls(urls)

    for post in posts:
        if mr.get_post_by_hash(post.hash_id) is None:
            mr.insert_post(post)
