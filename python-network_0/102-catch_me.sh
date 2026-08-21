#!/usr/bin/env bash
# Sends the required PUT request with the correct header and user ID.
curl -sL -X PUT -H "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me
