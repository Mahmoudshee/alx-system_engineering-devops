#!/usr/bin/python3
"""
This script contains a function that queries the Reddit API
and returns the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, returns 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "MyBot/0.0.1"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        json_data = response.json()
        return json_data["data"]["subscribers"]
    else:
        return 0

