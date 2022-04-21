#!/bin/bash
# curl to GET and display the body of URL
curl -s -o /dev/null -w "Route %{http_code}" https://www.google.com/
