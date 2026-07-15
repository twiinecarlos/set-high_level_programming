#!/usr/bin/python3
class Rectangle:
    """Defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print rectangle using #."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = ""
        for row in range(self.__height):
            rectangle += str(self.print_symbol) * self.__width
            if row != self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """Return string representation."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print message when deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return biggest rectangle based on area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError(
                "rect_1 must be an instance of Rectangle"
            )
        if not isinstance(rect_2, Rectangle):
            raise TypeError(
                "rect_2 must be an instance of Rectangle"
            )

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
