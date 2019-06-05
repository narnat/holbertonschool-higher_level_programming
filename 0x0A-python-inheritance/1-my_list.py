#!/usr/bin/python3
"""Simple My List class"""


class MyList(list):
    """Simple class, inherits from list"""

    def print_sorted(self):
        """Prints list sorted"""

        print(sorted(self))
