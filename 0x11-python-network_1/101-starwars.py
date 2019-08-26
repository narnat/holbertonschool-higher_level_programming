#!/usr/bin/python3
"""Python script that takes in a string and sends
a search request to the Star Wars API, with pagination"""
from sys import argv
import requests


if __name__ == "__main__":
    arg = ""
    if len(argv) == 2:
        arg = argv[1]
    try:
        r = requests.get('https://swapi.co/api/people/?search={}'.format(arg))
        j = r.json()
        if j:
            l = j.get('results')
            print('Number of results:', j.get('count'))
            while j.get('next'):
                r = requests.get(j.get('next'))
                j = r.json()
                l += j.get('results')
            for i in l:
                print(i.get('name'))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
