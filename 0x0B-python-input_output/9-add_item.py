#!/usr/bin/python3
"""Saves arguments as a json"""
from sys import argv
import os.path
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = 'add_item.json'
res = []
if os.path.exists(filename):
    res = load_from_json_file(filename)
save_to_json_file(res + argv[1:], filename)
