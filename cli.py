import requests
import json

from model.schema import Post

endpoint: str = "http://localhost:8000"


print("#" * 10)
print("#  NEWS  #")
print("#" * 10)
print("")


while True:

    response = requests.get(endpoint)
    json_object = json.loads(response.text)
    post: Post = Post(**json_object)

    vote = input("Did you like this post? (y/n)").lower()
    if vote == "y":
        print("user likes")
        post.rating = 1
    else:
        print("user dislikes")
        post.rating = 0

    requests.post(endpoint, post)
