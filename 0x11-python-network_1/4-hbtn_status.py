#!/usr/bin/python3
''' Python script that fetches a URL with package requests '''

import requests

if __name__ == "__main__":
    body = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(body.text)))
    print("\t- content: {}".format(body.text))
