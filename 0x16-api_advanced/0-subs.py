#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    # Define the URL for the subreddit about.json
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Define headers with a custom User-Agent
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; SubredditBot/1.0)'}
    
    try:
        # Perform the request to the Reddit API without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response and get the number of subscribers
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            # If the subreddit does not exist or there is an error, return 0
            return 0
    except requests.RequestException:
        # Handle any network or request issues by returning 0
        return 0

