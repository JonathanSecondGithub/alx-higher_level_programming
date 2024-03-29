#!/usr/bin/python3
"""Another square class"""

class Square:
    """class Square"""
    def __init__(self, size=0):
        """Args:
            size (int): square size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
    def area(self):
        return self.__size * self.__size
