#!/usr/bin/python3
"""Return the number of subscribers of a given subreddit"""
import requests

def number_of_subscribers(subreddit):
    """function that fetches number_of_subscribers"""
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        RESPONSE.raise_for_status()  # Raise exception for bad status codes

        data = RESPONSE.json().get("data")
        if data:
            return data.get("subscribers")
        else:
            return 0  # Subreddit data not found

    except requests.RequestException as e:
        print("Error accessing Reddit API:", e)
        return 0  # Return 0 in case of any error
    except Exception as e:
        print("Error:", e)
        return 0  # Return 0 for any unexpected error

# Test your function with different subreddits
print(number_of_subscribers("existing_subreddit"))
print(number_of_subscribers("nonexisting_subreddit"))

