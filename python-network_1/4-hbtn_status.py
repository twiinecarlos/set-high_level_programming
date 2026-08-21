#!/usr/bin/python3
"""Fetches the intranet status using requests."""

import requests


if __name__ == "__main__":
    try:
        response = requests.get(
            "https://alx-intranet.hbtn.io/status"
        )
    except requests.RequestException:
        response = requests.get(
            "https://intranet.hbtn.io/status"
        )

    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
