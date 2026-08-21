#!/usr/bin/env bash
# Displays all HTTP methods accepted by the server.
curl -sI -X OPTIONS "$1" | grep -i "^Allow:" | cut -d " " -f2-
