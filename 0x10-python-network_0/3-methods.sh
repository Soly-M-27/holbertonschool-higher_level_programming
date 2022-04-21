#!/bin/bash
# curl to display all HTTP methods the server will accept
curl -s -I $1 | grep "Allow:" | sed -ne 's/^Allow: //p'
