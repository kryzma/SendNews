from typing import List

from src.model import schema
from src.repository.posts import postsRepo, mongoRepo
from src.postSuggestor import mockPostSuggestor, postSuggestor

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def suggest_post():
    """
    Returns suggested post
    """

    print("inside get")

    pr: postsRepo.PostsRepository = mongoRepo.MongoPostsRepository()
    posts: List[schema.Post] = pr.get_unrated_posts()
    ps: postSuggestor.PostsSuggestor = mockPostSuggestor.MockPostsSuggestor()

    return ps.get_suggested_post(posts)


@app.post("/")
def suggest_post_response(post: schema.Post):
    """
    Takes in suggested post result
    """

    print("user posted!")

    ps: postSuggestor.PostsSuggestor = mockPostSuggestor.MockPostsSuggestor()
    ps.send_suggestion_result(post)



