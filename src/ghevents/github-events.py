#!/usr/bin/env python
import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'


def retrieve_events(url):
    """Download public GitHub events from the given API URL.

    Returns the parsed JSON response, normally a list of event dictionaries.
    """
    response_text = requests.get(url).text
    events = json.loads(response_text)
    return events


def print_events(events, n=5):
    """Print the first n events, one per line, as 'type :: repo'."""
    for x in events[:n]:
        event = x['type'] + ' :: ' + x['repo']['name']
        print(event)


def main():
    """Fetch and print recent GitHub events for GITHUB_USER."""
    print(GHUSER)
    print(url)
    events = retrieve_events(url)
    print_events(events)


if __name__ == "__main__":
    main()