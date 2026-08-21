#!/usr/bin/python3
"""Fetches the status of the intranet using urllib."""

import urllib.request


if __name__ == "__main__":
    urls = [
        "https://alx-intranet.hbtn.io/status",
        "https://intranet.hbtn.io/status"
    ]

    body = None

    for url in urls:
        try:
            with urllib.request.urlopen(url) as response:
                body = response.read()
            break
        except Exception:
            pass

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))
