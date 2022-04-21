#!/bin/bash
# Displays the size of the body of the response.
curl -so /dev/null https://www.google.com/ -w '%{size_download}\n'
