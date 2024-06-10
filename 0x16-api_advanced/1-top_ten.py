import requests

def number_of_subscribers(subreddit):
  """
  This function queries the Reddit API and returns the number of subscribers for a given subreddit.

  Args:
      subreddit: The name of the subreddit (without the 'r/').

  Returns:
      The number of subscribers for the subreddit, or 0 if the subreddit is invalid.
  """

  # Base URL for subreddit information
  url = f"https://www.reddit.com/r/{subreddit}/about.json?limit=0"  # limit=0 avoids extra data

  # Set a custom User-Agent header to avoid throttling
  headers = {"User-Agent": "My Reddit API Client v1.0 (by /u/your_username)"}

  # Send the GET request without following redirects
  try:
    response = requests.get(url, headers=headers, allow_redirects=False)
    response.raise_for_status()  # Raise an exception for non-200 status codes
  except requests.exceptions.RequestException:
    # Handle any request errors (e.g., network issues)
    return 0

  # Parse the JSON response
  data = response.json()

  # Check if the subreddit exists (data key 'data' may be missing for invalid subreddits)
  if 'data' not in data:
    return 0

  # Extract the subscriber count
  subscribers = data['data'].get('subscribers', 0)

  return subscribers

# Example usage
subreddit_name = "learnpython"
number_of_subs = number_of_subscribers(subreddit_name)

if number_of_subs > 0:
  print(f"The subreddit r/{subreddit_name} has {number_of_subs} subscribers.")
else:
  print(f"Subreddit r/{subreddit_name} is invalid or not found.")
