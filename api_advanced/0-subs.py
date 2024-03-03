import requests

def number_of_subscribers(subreddit):
    """Function that queries the Reddit API and returns the number of subscribers for a given subreddit."""
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}

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

