#!/usr/bin/python3
"""
Module for querying the Reddit API recursively and returning a list of titles of
all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of titles of all hot
    articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to search.
        hot_list (list): The list to append the hot article titles to.
        after (str): The fullname of the last item in the previous page of
            results.

    Returns:
        A list of titles of all hot articles for the given subreddit, or None if
        the subreddit is not found.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    # Handle pagination with the 'after' parameter
    params = {"limit": 100}
    if after:
        params["after"] = after

    # Send the GET request to the API and check for errors
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None

    # Extract the data from the JSON response
    data = response.json()["data"]
    children = data["children"]
    for child in children:
        title = child["data"]["title"]
        hot_list.append(title)

    # Recursively call the function with the 'after' parameter set to the
    # fullname of the last item in the previous page of results
    after = data["after"]
    if after:
        recurse(subreddit, hot_list, after)

    return hot_list
