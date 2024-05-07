#!/usr/bin/python3
"""
Script to retrieve the number of subscribers for a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the total number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers.
        0 if the subreddit is invalid or not found.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Reddit Subscribers Scraper/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
