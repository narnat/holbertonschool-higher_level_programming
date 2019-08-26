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
            print('Number of results:', j.get('count'))
            l = j.get('results')
            while j.get('next'):
                r = requests.get(j.get('next'))
                j = r.json()
                l += j.get('results')
            for i in l:
                print(i.get('name'))
                for a in i.get('films'):
                    film = requests.get(a)
                    print('\t', film.json().get('title'), sep="")
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
