#!/usr/bin/python3
''' Python script that takes your GitHub credentials
    (username and password) and uses the GitHub API
    to display your id '''

import sys
import requests

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    URL = 'https://api.github.com/user'
    body = requests.get(URL, auth=(user, passwd))
    print(body.json().get('id'))
