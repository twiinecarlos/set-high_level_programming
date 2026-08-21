#!/usr/bin/env bash
# Sends a JSON file in a POST request and displays the response body.
curl -sX POST -H "Content-Type: application/json" --data-binary "@$2" "$1"
