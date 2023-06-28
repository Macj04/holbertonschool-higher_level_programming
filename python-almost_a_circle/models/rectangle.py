#!/usr/bin/python3
''' Write the class Rectangle that inherits from Base  '''


from models.base import Base


class Rectangle(Base):
    ''' class  '''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = self.__height = self.__x = self.__y = 0
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ''' area of rectangle  '''
        return self.__height * self.__width

    def display(self):
        ''' print a rectangle '''
        for _ in range(self.__y):
            print('')
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(' ', end='')
            for _ in range(self.__width):
                print('#', end='')
            print('')

    def __str__(self):
        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}'

    def update(self, *args, **kwargs):
        '''Update the Rectangle'''
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if key in ['id', 'width', 'height', 'x', 'y']:
                    setattr(self, key, value)

    def to_dictionary(self):
        ''' to dict '''
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
