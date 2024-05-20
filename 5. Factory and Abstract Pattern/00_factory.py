'''
Intro : This pattern is used when on conditional base we have to create obj.

So what we do in this pattern is, we will have an abstract class responsible
for creating obj and it will maintain has-a relationship with some class
'''

from abc import abstractmethod, ABC
from typing import Any
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print('circle')

class Square(Shape):
    def draw(self):
        print('Square')

class Rectangle(Shape):
    def draw(self):
        print('Rectangle')

class IShapeFactory(ABC):
    @abstractmethod
    def createShapeBySomeLogic(self):
        pass

class ShapeCreator1(IShapeFactory):
    def createShapeBySomeLogic(self) -> Shape:
        # do some business logic and return required class obj
        return Rectangle()

class ShapeCreator2(IShapeFactory):
    def createShapeBySomeLogic(self) -> Shape:
        # do some business logic and return required class obj
        return Circle()

if __name__ == '__main__':
    shape_creator_1 = ShapeCreator1()
    shape_obj_1 = shape_creator_1.createShapeBySomeLogic()
    shape_obj_1.draw()

    shape_creator_2 = ShapeCreator2()
    shape_obj_2 = shape_creator_2.createShapeBySomeLogic()
    shape_obj_2.draw()