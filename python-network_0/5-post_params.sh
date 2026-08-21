#!/usr/bin/env bash
# Sends a POST request with the required email and subject parameters.
curl -sX POST -d "email=test@gmail.com" \
    -d "subject=I will always be here for PLD" "$1"
