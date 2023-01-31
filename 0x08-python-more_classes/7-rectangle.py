#!/usr/bin/python3
"""Rectangle module.

This module contains a class that defines a rectangle.

"""


class Rectangle():
    """Defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """__init__

        Initializing instance of a triangle
        private instance attributes: width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """similar as my_print"""
        msg = []
        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    msg.append("#")
                if i < self.__height - 1:
                    msg.append('\n')
        return ''.join(msg)

    def __repr__(self):
        m = "{}({}, {})"
        return(m.format(self.__class__.__name__, self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
