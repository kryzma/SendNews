import requests
import json

endpoint: str = "http://localhost:8000"


print("#" * 10)
print("#  NEWS  #")
print("#" * 10)
print("")


while True:

    response = requests.get(endpoint)
    json_object = json.dumps(response.text)
    vote = input("Did you like this post? (y/n)").lower()

    if vote == "y":
        print("user likes")
    else:
        print("user dislikes")

    requests.post(endpoint, )
