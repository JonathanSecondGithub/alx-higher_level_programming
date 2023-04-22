#!/usr/bin/python3
"""Another square class"""

class Square:
    """class Square"""
    def __init__(self, size = 0):
        if size < 0:
            raise ValueError("Size cannot be less than 0")
        if type(size) != int:
            raise TypeError("")
        self.size = __size

