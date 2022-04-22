#!/usr/bin/python3
# Python script that fetches https://intranet.hbtn.io/status.
import urllib.request
import sys

try:
    with urllib.request.urlopen(sys.argv[1]).encode('utf-8') as response:
        body = response.read()
        print("{}".format(body.decode('utf-8')))
except urllib.error.HTTPError:
    x = urllib.request.get(sys.argv[1])
    print("Error code: {}".format(x.status_code))