'''
Issue - Suppose we a class Parent and it implements a method called f, and Parent class has several
child classes which inherits method f, but few classes choose to override the method with their
own implementation, and those implementation overlaps with each other (meaning they are same code)
so in real we are creating duplicate codes, to resolve this we use Strategy Pattern.

Here first we will create an issue and then later resolve it with Strategy Pattern (No Rocket Science)
'''
class Parent:
    def f(self):
        print("Parent method")

class Child1(Parent):
    def f(self):
        print("Overriding Parent method")

class Child2(Parent):
    pass

class Child3(Parent):
    def f(self):
        print("Overriding Parent method")

child1_obj = Child1()
# child1_obj.f() # Overriding Parent method

child1_obj = Child2()
# child1_obj.f() # Parent method

child1_obj = Child3()
# child1_obj.f() # Overriding Parent method



'''
Strategy Pattern lets us to define a family of algorithms and put them into a separate
class and make their objects interchangeable.


'''

from abc import abstractmethod

class IAlgo:
    @abstractmethod
    def algo(self):
        pass

class Algo1(IAlgo):
    def algo(self):
        print("first algorithm")

class Algo2(IAlgo):
    def algo(self):
        print("second algorithm")

class Parent:
    def __init__(self, algo: IAlgo):
        self._algo: IAlgo = algo

    @property
    def algorithm(self):
        return self._algo
    
    @algorithm.setter
    def algorithm(self, algo: IAlgo):
        self._algo = algo

    def f(self):
        self.algorithm.algo()

class Child1(Parent):
    pass

class Child2(Parent):
    pass

class Child3(Parent):
    pass

child1_obj = Child1(Algo1())
child1_obj.f() # first algorithm
child2_obj = Child2(Algo2())
child2_obj.f() # second algorithm
child3_obj = Child3(Algo1())
child3_obj.f() # first algorithm
