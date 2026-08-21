#!/usr/bin/python3
"""Displays the 10 most recent commits of a GitHub repository."""

import sys

import requests


if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(
        owner,
        repository
    )

    response = requests.get(
        url,
        params={"per_page": 10}
    )

    commits = response.json()

    for commit in commits[:10]:
        sha = commit.get("sha")
        author = commit.get("commit", {}).get("author", {}).get("name")
        print("{}: {}".format(sha, author))
