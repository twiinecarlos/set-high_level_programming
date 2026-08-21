#!/usr/bin/python3
"""Sends an email address in a POST request using urllib."""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    data = urllib.parse.urlencode(
        {"email": sys.argv[2]}
    ).encode("utf-8")

    request = urllib.request.Request(
        sys.argv[1],
        data=data
    )

    with urllib.request.urlopen(request) as response:
        body = response.read()

    print(body.decode("utf-8"))
