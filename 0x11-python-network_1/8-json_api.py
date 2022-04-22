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

    try:
        b = requests.post('http://0.0.0.0:5000/search_user', param)
        if b.json().get('id') is not None:
            print("[{}] {}".format(b.json().get('id'), b.json().get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
