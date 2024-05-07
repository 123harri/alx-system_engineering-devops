#!/usr/bin/python3
"""
Module to recursively retrieve the titles of all hot
articles for a specified Reddit subreddit.
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively retrieves the titles of all hot
    articles for a specified subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot articles.

    Returns:
        list: A list containing the titles of all hot articles.
        None if no results are found for the given subreddit.
    """
    if len(hot_list) == 100 or subreddit is None:
        return hot_list
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "Reddit Hot Articles Retriever/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])
        if 'after' in data['data'] and data['data']['after'] is not None:
            return recurse(subreddit, hot_list)
        else:
            return hot_list
    else:
        return None


if __name__ == "__main__":
    subreddit = input("Enter the name of the subreddit: ")
    result = recurse(subreddit)
    if result is not None:
        print(len(result))
    else:
        print("None")
