import requests
import json

from src.model.schema import Post

endpoint: str = "http://damp-bush-784.fly.dev"


print("#" * 10)
print("#  NEWS  #")
print("#" * 10)
print("")


while True:

    response = requests.get(endpoint)
    json_object = json.loads(response.text)
    post: Post = Post(**json_object)

    print(post.title)
    vote = input("Did you like this post? (y/n)").lower()
    if vote == "y":
        print("user likes")
        post.rating = 1
    else:
        print("user dislikes")
        post.rating = 0

    json_obj: str = post.to_json()
    requests.post(endpoint, json_obj)
