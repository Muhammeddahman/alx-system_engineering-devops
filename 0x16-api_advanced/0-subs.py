#!/usres Reddit API to print the number of subscribers of a subreddit
"""
import requests
"""

def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit
    """
    url = f"https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
	"User-Agent": "Linux:0x16.api.advanced:v1.0.0 (by /u/bdov_"
}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0

    results = responce.json().get("data")
    return results.get("subscribers")
