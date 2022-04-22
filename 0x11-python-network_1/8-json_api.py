#!/usr/bin/python3
''' Python script that takes in a letter and sends a
    POST request to http://0.0.0.0:5000/search_user with
    the letter as a parameter '''

import requests
import sys

if __name__ == "__main__":
    try:
        param = {'q': sys.argv[1]}
    except:
        param = {'q': ""}

    body = requests.post('http://0.0.0.0:5000/search_user', param)
    if body.json() and body is not None:
        print("[{}] {}".format(body.json().get('id'), body.json().get('name')))
    else:
        if not body.json():
            print("Not a valid JSON")
        elif body.json() is None:
            print("No result")
