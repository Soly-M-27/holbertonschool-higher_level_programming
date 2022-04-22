#!/usr/bin/python3
''' Python script that takes in a URL, sends a request to the URL
    and displays the body of the response'''

import requests
import sys

if __name__ == "__main__":
    body = requests.get(sys.argv[1])
    if body.status_code >= 400:
        print("Error code: {}".format(body.status_code))
    else:
        print(body)
