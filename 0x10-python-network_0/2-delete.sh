#!/bin/bash
# curl sends DELETE request to URL and displays response
curl -s -X DELETE $1 -w "I'm a DELETE request"
