#!/usr/bin/python3
"""Rectangle module.

This module contains a class that defines a rectangle.

"""


class Rectangle():
    """Defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Sets the necessary attributes for the Rectangle object.

        Args:

            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """Returns the current rectangle area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the current rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Return the printable representation of the Rectangle.
        
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

            rect = []
            for i in range(self.__height):
                [rect.append('#') for j in range(self.__width)]
                if i != self.__height - 1:
                    rect.append("\n")
            return ("".join(rect))
