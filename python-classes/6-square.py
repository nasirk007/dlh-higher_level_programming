#!/usr/bin/python3
"""This is a module for creating class Square"""


class Square:
    """This class is calculating the area of a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing for missing size and position default 0"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter Size"""
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """Getter Property"""
        return self.__position

    @position.setter
    def position(self, position):
        if (
            not isinstance(position, tuple) or len(position) != 2
            or not all(isinstance(i, int) and i >= 0 for i in position)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        area = self.__size ** 2
        return area

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            if self.__position[1] > 0:
                for k in range(self.__position[1]):
                    print("")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
