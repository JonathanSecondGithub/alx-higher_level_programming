#!/usr/bin/python3
"""Defines a Rectangle Class"""
from models.base import Base

class Rectangle(Base):
    """Represents a Rectangle"""
    
     def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
           
           Args:
                width (int): The width of the new Rectangle.
                height (int): The height of the new Rectangle.
                x (int): The x coordinate of the new Rectangle.
                y (int): The y coordinate of the new Rectangle.
                id (int): The identity of the new Rectangle.
        """
        self.width = width
        self.height = height
        self.x = x  self.y = y
        super.__init__(id)

    @property    
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x attribute of the rectangle"""
        return self.__x

    @x.setter
    def x(self,value):
        """set the x attribute of the rectangle"""
        self.__x = value

    @property
    def y(self, value):
        """get the y attribute of the rectangle"""
        return self.__y

    @y.setter
    def y(self,value):
        """set the y attribute of the rectangle"""
        self.__y = value
