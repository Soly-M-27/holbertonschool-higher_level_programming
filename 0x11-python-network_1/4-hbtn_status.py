#!/usr/bin/python3
''' Python script that fetches a URL with package requests '''

import requests

with requests.get('https://intranet.hbtn.io/status') as res:
    print("Body response:")
    print("\t- type:", type(res.text))
    print("\t- content:", res.text)
