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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    def my_print(self):
        x = self.size
        while x > 0:
            y = self.size
            while y > 0:
                print("{}".format("#"), end = '')
                y = y - 1
            print()
            x = x - 1
            
