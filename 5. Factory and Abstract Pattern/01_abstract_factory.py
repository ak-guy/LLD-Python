from __future__ import annotations
from abc import ABC, abstractmethod

# # # Products Abstract class and their childs implementation begins # # #

# # # Product 1 # # #
class IAProduct(ABC):
    @abstractmethod
    def dummy_func(self):
        pass

class IAProduct1(IAProduct):
    def dummy_func(self):
        return 1

class IAProduct2(IAProduct):
    def dummy_func(self):
        return 1
    
class IAProduct3(IAProduct):
    def dummy_func(self):
        return 1
    
# # # Product 2 # # #
class IBProduct(ABC):
    @abstractmethod
    def dummy_func(self):
        pass

class IBProduct1(IBProduct):
    def dummy_func(self):
        return 1

class IBProduct2(IBProduct):
    def dummy_func(self):
        return 1
    
class IBProduct3(IBProduct):
    def dummy_func(self):
        return 1

# # # Products Abstract class and their childs implementation ends # # #

# ---------------------------------------- # ------------------------------------------#

# # # Factory Method to handle Product A/B object creation implementation begins # # #

# # # Factory Method to handle A object creation # # #
class IFactoryA(ABC):
    @abstractmethod
    def createABasedOnSomeLogic(self) -> IAProduct:
        pass

class FactoryA1(IFactoryA):
    def createABasedOnSomeLogic(self) -> IAProduct:
        # do some bussiness logic and return IAProduct's child object
        pass

class FactoryA2(IFactoryA):
    def createABasedOnSomeLogic(self) -> IAProduct:
        # do some bussiness logic and return IAProduct's child object
        pass

# # # Factory Method to handle B object creation # # #
class IFactoryB(ABC):
    @abstractmethod
    def createBBasedOnSomeLogic(self) -> IBProduct:
        pass

class FactoryB1(IFactoryB):
    def createBBasedOnSomeLogic(self) -> IBProduct:
        # do some bussiness logic and return IAProduct's child object
        pass

class FactoryB2(IFactoryB):
    def createBBasedOnSomeLogic(self) -> IBProduct:
        # do some bussiness logic and return IAProduct's child object
        pass

# # # Factory Method to handle Product A/B object creation implementation ends # # #


# -------------------------------------------- # --------------------------------------#

# # # Actual Factory method responsible for creating objects of both A and B # # #
class IMainFactory(ABC):
    @abstractmethod
    def getAFactory(self, a_factory_obj: IFactoryA) -> IAProduct:
        pass

    @abstractmethod
    def getBFactory(self, b_factory_obj: IFactoryB) -> IBProduct:
        pass

class MainFactory1(IMainFactory):
    def getAFactory(self, a_factory_obj: IFactoryA) -> IAProduct:
        return a_factory_obj.createABasedOnSomeLogic()

    def getBFactory(self, b_factory_obj: IFactoryB) -> IBProduct:
        return b_factory_obj.createBBasedOnSomeLogic()


# ---------------------------------------------- # ------------------------------------#

if __name__ == '__main__':
    main_factory_obj = MainFactory1()
    a_obj_1 = main_factory_obj.getAFactory(FactoryA1())
    a_obj_2 = main_factory_obj.getAFactory(FactoryA2())

    b_obj_1 = main_factory_obj.getBFactory(FactoryB1())
    b_obj_2 = main_factory_obj.getBFactory(FactoryB2())
