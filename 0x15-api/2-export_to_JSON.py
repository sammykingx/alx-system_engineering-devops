#!/usr/bin/python3

import json
import requests as r
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    usr = r.get(url + "users/{}".format(user_id)).json()
    username = usr.get("username")
    to_do = r.get(url + "todos", params={"user_id": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{"task": e.get("title"),
                              "completed": e.get("completed"),
                              "username": username} for e in to_do]},
                  jsonfile)
