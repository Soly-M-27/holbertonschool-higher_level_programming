#!/usr/bin/python3
''' Python script that fetches a URL with package requests '''

import requests

if __name__ == "__main__":
    with requests.get('https://intranet.hbtn.io/status') as res:
        print("Body response:")
        print("\t- type: {}".format(type(res.text)))
        print("\t- content: {}".format(res.text))
