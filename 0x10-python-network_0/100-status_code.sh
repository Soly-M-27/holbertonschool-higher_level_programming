#!/bin/bash
# Display HTTP status code
curl -s -o /dev/null -w "%{http_code}" $1
