#!/usr/bin/python3
"""Return the number of subscribers of a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """function that fetches number_of_subscribers"""
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    data = response.json()
    subscribers = data.get("data", {}).get("subscribers", 0)
    return subscribers, "OK"
  except requests.exceptions.RequestException as e:
    # Handle any request-related errors
    return 0, f"Error: {e}"
  except Exception as e:
    # Catch unexpected errors
    return 0, f"Error: Unexpected error - {e}"

# Example usage with output messages
existing_subreddit, message = number_of_subscribers("programming")
print(f"Existing Subreddit: {message}")  

nonexistent_subreddit, message = number_of_subscribers("notarealone")
print(f"Non-existent Subreddit: {message}")  
