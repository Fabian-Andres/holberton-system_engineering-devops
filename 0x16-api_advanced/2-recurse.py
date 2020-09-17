#!/usr/bin/python3
"""
    Funtion that print title of first 10 hot post
"""
import json
import requests
url = 'https://www.reddit.com/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}


def recurse(subreddit, hot_list=[], after=' '):
    query = '/hot.json?limit=100&after='
    url_subreddit = (url + '/r/' + subreddit + query + after)

    # Get data response whit requests
    r_subreddit = requests.get(url_subreddit, headers=headers)
    if r_subreddit.status_code != 200:
        return None

    # Set string to JSON
    obj_subreddit = r_subreddit.json()

    for children in obj_subreddit['data']['children']:
        hot_list.append(children['data']['title'])

    after = obj_subreddit['data']['after']
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
