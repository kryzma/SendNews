import postSuggestor.postSuggestor
import repository.posts as posts_repository
import postSuggestor
import mockPostSuggestor
from model import schema

from typing import List


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def suggest_post():
    """
    Returns suggested post
    """

    pr: posts_repository.postsRepo.PostsRepository = posts_repository.mongoRepo.MongoPostsRepository()
    posts: List[schema.Post] = pr.get_unrated_posts()
    ps: postSuggestor.PostsSuggestor = mockPostSuggestor.MockPostsSuggestor()

    return ps.get_suggested_post(posts)


@app.post("/")
def suggest_post_response():
    """
    Takes in suggested post result
    """
    return {"hi"}


