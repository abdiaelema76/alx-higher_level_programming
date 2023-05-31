#!/usr/bin/python3

class Square:
    """Module that defines a square by: (based on 5-square.py)"""
    def __init__(self, size=0, position=(0, 0)):
        """initialization of Square.
        Args:
            size: a size of a square
            position: where square is
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """get/set current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__-size = value

    @property
    def position(self):
        """retrievs  private instance"""
        return (self.__position)
    
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all (isinstance(num, int) for num in value) or
            not all(num >= for num in value)):
            raise TypeError("position must be a tuple of two positive intergers")
        self.__position = value

    def area(self):
        """ returns the current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print("", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
