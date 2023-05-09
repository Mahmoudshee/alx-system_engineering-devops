#!/usr/bin/python3

"""
Queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    """
    Recursive function that queries the Reddit API,
    parses the title of all hot articles,
    and prints a sorted count of given keywords.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/58.0.3029.110 Safari/537.3'}
    params = {'limit': 100, 'after': after}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    hot_posts = data.get('data', {}).get('children', [])

    if not hot_posts:
        return None

    for post in hot_posts:
        title = post.get('data', {}).get('title', '').lower()
        words = title.split()

        for word in words:
            word = word.rstrip('!,.?_').lower()
            if word in word_list and word not in hot_list:
                count = words.count(word)
                hot_list += [word] * count

    next_page = data.get('data', {}).get('after', None)
    if next_page:
        count_words(subreddit, word_list, hot_list, next_page)

    if not after:
        word_count = {word: 0 for word in word_list}
        for word in hot_list:
            word_count[word] += 1

        sorted_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for item in sorted_count:
            if item[1] != 0:
                print('{}: {}'.format(item[0], item[1]))
