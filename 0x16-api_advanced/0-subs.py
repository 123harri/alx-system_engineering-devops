#!/usr/bin/python3
"""
Module to retrieve the number of subscribers for a specified Reddit subreddit.
"""

import sys
import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers.
        0 if the subreddit is invalid or not found.
    """
    # Construct the URL for the subreddit's information JSON
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Reddit Subscribers Counter/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0

# Example usage:
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the name of the subreddit as a command line argument.")
    else:
        subreddit = sys.argv[1]
        print(number_of_subscribers(subreddit))
