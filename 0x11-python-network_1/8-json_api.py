#!/usr/bin/python3
''' Python script that takes in a letter and sends a
    POST request to http://0.0.0.0:5000/search_user with
    the letter as a parameter '''

import requests
import sys

if __name__ == "__main__":
    args = sys.argv
    try:
        if len(args) == 0:
            print("No result")
    except:
        try:
            jsonvar = {'q': sys.argv[1]}
        except:
            jsonvar = {'q': ""}

        body = requests.post('http://0.0.0.0:5000/search_user', jsonvar)
        if body.json() and body is not None:
            print("[{}] {}".format(body.json().get('id'), body.json().get('name')))
        else:
            if not body.json():
                print("Not a valid JSON")
            elif body.json() == "":
                print("No result")
