from abc import ABC, abstractmethod


# # # Abstract Pizza_base class # # #
class IBasePizza(ABC):
    @abstractmethod
    def cost(self):
        pass

class FarmHouse(IBasePizza):
    def cost(self):
        return 100
    
class VegieDelight(IBasePizza):
    def cost(self):
        return 150
    
class Margherita(IBasePizza):
    def cost(self):
        return 200
    


# # # Abstract Topping class (will inherit IBasePizza class) # # #
class IToppingsDecorator(IBasePizza, ABC):
    @abstractmethod
    def cost():
        pass

class ExtraCheese(IToppingsDecorator):
    def __init__(self, base_pizza: IBasePizza):
        self._base_pizza = base_pizza

    def getBasePizzaCost(self):
        return self._base_pizza.cost()
    
    def cost(self):
        return self.getBasePizzaCost() + 20
    
class Mushroom(IToppingsDecorator):
    def __init__(self, base_pizza: IBasePizza):
        self._base_pizza = base_pizza

    def getBasePizzaCost(self):
        return self._base_pizza.cost()
    
    def cost(self):
        return self.getBasePizzaCost() + 40
    
class IDipsDecorator(IBasePizza, ABC):
    @abstractmethod
    def cost():
        pass

class ShrimpDips(IDipsDecorator):
    def __init__(self, base_pizza: IBasePizza):
        self._base_pizza = base_pizza

    def getBasePizzaCost(self):
        return self._base_pizza.cost()
    
    def cost(self):
        return self.getBasePizzaCost() + 5

class HotCornDips(IDipsDecorator):
    def __init__(self, base_pizza: IBasePizza):
        self._base_pizza = base_pizza

    def getBasePizzaCost(self):
        return self._base_pizza.cost()
    
    def cost(self):
        return self.getBasePizzaCost() + 10


if __name__ == '__main__':
    base_pizza = Margherita()
    pizza_topping = ShrimpDips(HotCornDips(ExtraCheese(Mushroom(base_pizza))))
    print(pizza_topping.cost())