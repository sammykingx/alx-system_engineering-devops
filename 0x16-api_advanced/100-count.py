#!/usr/bin/python3
"""
Module to request information from reditt API about any subreddit recursively
"""
import requests


def counter(word_list, hot_list):
    """
    count the number of word in the titles
    """
    words_count = {}
    for item in word_list:
        words_count[item.lower()] = 0
    for word in word_list:
        word = word.lower()
        for title in hot_list:
            title_words = title.split()
            for item in title_words:
                if word == item:
                    words_count[word] += 1
    for key, value in sorted(words_count.items(), key=lambda x: (-x[1], x[0])):
        if value != 0:
            print("{}: {}".format(key, value))
    return(None)


def count_words(subreddit, word_list, hot_list=[], params={}):
    """
    Method to request reddit API and prints a sorted count of given keywords
    passed as command arguments.
    """
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    headers = {
        'User-agent': "just me"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return (None)

    information = response.json()
    data = information["data"]
    children = data["children"]
    for post in children:
        hot_list.append(post["data"]["title"].lower())
    params["after"] = data["after"]

    if params["after"] is not None:
        count_words(subreddit, word_list, hot_list, params)
    else:
        counter(word_list, hot_list)
