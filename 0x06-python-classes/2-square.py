#!/usr/bin/python3
"""Another square class"""

class Square:
    """class Square"""
    def __init__(self, size = 0):
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(size) != int:
            raise TypeError("size must be an integer")
        self.size = __size

