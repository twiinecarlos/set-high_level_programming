#!/usr/bin/env bash
# Makes the required request and follows redirects with user_id 98.
curl -sL -X PUT -H "user_id: 98" 0.0.0.0:5000/catch_me
