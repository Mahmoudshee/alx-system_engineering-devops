#!/usr/bin/python3
"""Top Ten"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit."""

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    json_data = response.json()
    children = json_data.get('data', {}).get('children', None)

    if not children:
        print(None)
        return

    for i, post in enumerate(children):
        if i == 10:
            break
        print(post.get('data', {}).get('title', None))
