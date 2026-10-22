from abc import ABC, abstractmethod

class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.topping = None

    def __str__(self):
        return f"Pizza(dough='{self.dough}', sauce='{self.sauce}', topping='{self.topping}')"

class PizzaBuilder(ABC):
    @abstractmethod
    def build_dough(self):
        pass

    @abstractmethod
    def build_sauce(self):
        pass

    @abstractmethod
    def build_topping(self):
        pass

    @abstractmethod
    def get_result(self):
        pass

class HawaiianPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def build_dough(self):
        self.pizza.dough = "cross"

    def build_sauce(self):
        self.pizza.sauce = "mild"

    def build_topping(self):
        self.pizza.topping = "ham+pineapple"

    def get_result(self):
        return self.pizza

class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_pizza(self):
        self.builder.build_dough()
        self.builder.build_sauce()
        self.builder.build_topping()

if __name__ == "__main__":
    builder = HawaiianPizzaBuilder()
    director = PizzaDirector(builder)

    director.construct_pizza()
    pizza = builder.get_result()

    print(pizza)