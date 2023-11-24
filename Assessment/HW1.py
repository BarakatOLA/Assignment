#task 2
import abc
class shape(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def calc_perimeter(self,input):
        """Method documentation"""
        return
class Triangle(shape):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def calc_perimeter(self):
        perim = self.a +self.b +self.c
        print("consider me implemented", perim)
        return perim
class rectangle(shape):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def calc_perimeter(self):
        perim = self.a +self.b
        print("consider me implemented", perim)
        return perim
class square(rectangle):
    def __init__(self,a):
        super().__init__(a, a)
triangle_instance = Triangle(4, 8, 7)
rectangle_instance = rectangle(3, 9)
square_instance = square(8)

# Calling the calc_perimeter method for each instance
triangle_instance.calc_perimeter()
rectangle_instance.calc_perimeter()
square_instance.calc_perimeter()
