#!/bin/bash
# Cause server to respond with string
curl -s 0.0.0.0:5000/catch_me -w "You got me!"
