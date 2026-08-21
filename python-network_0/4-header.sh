#!/usr/bin/env bash
# Sends a GET request with the required X-School-User-Id header.
curl -sH "X-School-User-Id: 98" "$1"
