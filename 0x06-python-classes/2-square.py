#!/usr/bin/python3
"""Another square class"""

class Square:
    """class Square"""
    def __init__(self, size=0):
        try:
            self.size = __size
        except ValueError as e:
                    print("size must be >= 0")
        except TypeError as e:
            print("size must be an integer")

