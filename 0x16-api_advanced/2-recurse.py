#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively retrieves all hot posts for a given subreddit.

    subreddit: the subreddit to retrieve posts from.
    hot_list: list to store post titles.
    after: pagination parameter to continue from the last post retrieved.

    returns: list of post titles, or None if an invalid subreddit was given.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None

    data = response.json().get('data')
    if not data:
        return hot_list

    posts = data.get('children')
    if not posts:
        return hot_list

    for post in posts:
        title = post.get('data', {}).get('title')
        if title:
            hot_list.append(title)

    next_page = data.get('after')
    if not next_page:
        return hot_list

    return recurse(subreddit, hot_list, next_page)
