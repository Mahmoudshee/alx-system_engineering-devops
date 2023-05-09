#!/usr/bin/python3
"""
Module that queries the Reddit API recursively and prints a sorted count of
given keywords (case-insensitive, delimited by spaces. Javascript should count
as javascript, but java should not).
"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursive function that queries the Reddit API, parses the title of all hot
    articles, and prints a sorted count of given keywords.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyBot/0.0.1'}

    if after is None:
        params = {'limit': 100}
    else:
        params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data')
    after = data.get('after')

    for child in data.get('children'):
        title = child.get('data').get('title')
        title_list = title.lower().split()

        for word in word_list:
            count = title_list.count(word.lower())

            if count != 0:
                if word in word_count:
                    word_count[word] += count
                else:
                    word_count[word] = count

    if after is None:
        sorted_list = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for pair in sorted_list:
            print("{}: {}".format(pair[0], pair[1]))
    else:
        count_words(subreddit, word_list, after, word_count)
