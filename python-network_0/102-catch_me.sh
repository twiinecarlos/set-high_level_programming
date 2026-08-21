#!/usr/bin/env bash
# Makes the catch_me request with the required user ID header.
curl -sL -X PUT -H "X-School-User-Id: 98" 0.0.0.0:5000/catch_me
