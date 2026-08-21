#!/usr/bin/env bash
# Makes the required request and follows redirects to display the final response.
curl -sL -X PUT -H "Origin: School" 0.0.0.0:5000/catch_me
