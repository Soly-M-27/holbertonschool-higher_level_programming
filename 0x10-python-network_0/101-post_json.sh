#!/bin/bash
# Curl to send a JSON POST request to a URL
curl -s -X POST $1 -H "Content-Type: application/json" -d $2
