#!/usr/bin/python3
"""Return the number of subscribers of a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """function that fetches number_of_subscribers"""
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    else:
        return 0
