#!/usr/bin/env bash
# Sends a request to a URL and displays only the HTTP status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
