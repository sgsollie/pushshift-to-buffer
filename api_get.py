import requests
import json
import os

def pull_images(requestUrl):
    resp = requests.get(requestUrl)
    if resp.status_code != 200:
        # Just die if we don't get what we want. Dramatic I know.
        raise requests.HTTPError('GET /reddit/search/submission  {}'.format(resp.status_code))
        #f.close()
        os._exit(1)

    jsonresponse = resp.json()["data"]

    for val in jsonresponse:
        print(val["url"])

    return



print(pull_images("https://api.pushshift.io/reddit/search/submission/?subreddit=memes&sort=desc&sort_type=score&size=1"))
