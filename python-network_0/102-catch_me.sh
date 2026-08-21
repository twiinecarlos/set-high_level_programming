#!/usr/bin/env bash
# Makes the required request to catch the server and display its response.
curl -sX PUT -H "Origin: School" 0.0.0.0:5000/catch_me
