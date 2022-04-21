#!/bin/bash
# curl to display all HTTP methods the server will accept
curl -s -i -X OPTIONS $1
