#!/usr/bin/python3
''' Python script that fetches https://intranet.hbtn.io/status '''

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            body = response.read()
        print("{}".format(body.decode('utf-8')))
    except urllib.error.HTTPError as x:
        print("Error code: {}".format(x.status_code))
