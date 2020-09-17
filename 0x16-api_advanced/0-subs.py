#!/usr/bin/python3
"""
    Funtion that print number of subscribers if subredit exist
"""
import json
import requests


def number_of_subscribers(subreddit):

    # URL's to get all information
    url = 'https://www.reddit.com/'
    url_subreddit = (url + '/r/' + subreddit + '/about.json')
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

    # Get data response whit requests
    r_subreddit = requests.get(url_subreddit, headers=headers)
    # Set string to JSON
    obj_subreddit = r_subreddit.json()

    # Print number of subscribers
    if 'subscribers' in obj_subreddit['data']:
        subscribers = obj_subreddit['data']['subscribers']
        return (subscribers)
    else:
        return 0
