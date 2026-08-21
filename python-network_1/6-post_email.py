#!/usr/bin/python3
"""Sends an email address in a POST request using requests."""

import sys

import requests


if __name__ == "__main__":
    response = requests.post(
        sys.argv[1],
        data={"email": sys.argv[2]}
    )
    print(response.text)
