#!/usr/bin/python3
"""Return the number of subscribers of a given subreddit"""
import requests

def number_of_subscribers(subreddit):
    """Function that queries the Reddit API and returns the number of subscribers for a given subreddit."""
    
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data")
            if data:
                return data.get("subscribers", 0)
        elif response.status_code == 404:
            print("Invalid subreddit:", subreddit)
        else:
            print("Error:", response.status_code)
    except requests.RequestException as e:
        print("Request error:", e)
    except Exception as e:
        print("Error:", e)

    return 0


# Example usage
if __name__ == "__main__":
    subreddit = input("Enter the subreddit name: ")
    print("Number of subscribers:", number_of_subscribers(subreddit))

