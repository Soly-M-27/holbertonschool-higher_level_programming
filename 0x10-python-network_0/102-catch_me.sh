#!/bin/bash
# Cause server to respond with string
curl -s -o /dev/null -w "You got me!" '0.0.0.0:5000/catch_me'
