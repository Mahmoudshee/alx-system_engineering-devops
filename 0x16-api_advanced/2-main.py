#!/usr/bin/python3
"""
2-main
"""
import sys
from typing import List
from requests.exceptions import HTTPError

if __name__ == '__main__':
    recurse = __import__('2-recurse').recurse
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        try:
            result = recurse(subreddit)
            if result is not None:
                print(f"Retrieved {len(result)} hot posts from r/{subreddit}")
                print('\n'.join(result))
            else:
                print(f"No hot posts found for r/{subreddit}")
        except HTTPError:
            print(f"Error: r/{subreddit} is an invalid subreddit.")
