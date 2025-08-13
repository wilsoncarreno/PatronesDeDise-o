# 1️⃣ Product
class Burger:
    def __init__(self):
        self.bread = None
        self.meat = None
        self.cheese = None
        self.veggies = []
        self.sauce = None

    
# 2️⃣ Abstract Builder
from abc import ABC, abstractmethod

class BurgerBuilder(ABC):
    def __init__(self):
        self.burger = Burger()

    @abstractmethod
    def add_bread(self): pass

    @abstractmethod
    def add_meat(self): pass

    @abstractmethod
    def add_cheese(self): pass

    @abstractmethod
    def add_veggies(self): pass

    @abstractmethod
    def add_sauce(self): pass

    def get_burger(self):
        return self.burger

# 3️⃣ Concrete Builders
class ClassicBurgerBuilder(BurgerBuilder):
    def add_bread(self):
        self.burger.bread = "Sesame bun"
    def add_meat(self):
        self.burger.meat = "Beef"
    def add_cheese(self):
        self.burger.cheese = "Cheddar"
    def add_veggies(self):
        self.burger.veggies = ["Lettuce", "Tomato"]
    def add_sauce(self):
        self.burger.sauce = "Ketchup"

class VeganBurgerBuilder(BurgerBuilder):
    def add_bread(self):
        self.burger.bread = "Whole grain bun"
    def add_meat(self):
        self.burger.meat = "Plant-based patty"
    def add_cheese(self):
        self.burger.cheese = "Vegan cheese"
    def add_veggies(self):
        self.burger.veggies = ["Lettuce", "Tomato", "Onion"]
    def add_sauce(self):
        self.burger.sauce = "Vegan mayo"

# 4️⃣ Director
class BurgerDirector:
    def __init__(self, builder: BurgerBuilder):
        self.builder = builder

    def construct_burger(self):
        self.builder.add_bread()
        self.builder.add_meat()
        self.builder.add_cheese()
        self.builder.add_veggies()
        self.builder.add_sauce()
        return self.builder.get_burger()

# 5️⃣ Client Code
if __name__ == "__main__":
    # Classic Burger
    classic_builder = ClassicBurgerBuilder()
    director = BurgerDirector(classic_builder)
    burger1 = director.construct_burger()
    print("🍔 Classic Burger:", burger1)

    # Vegan Burger
    vegan_builder = VeganBurgerBuilder()
    director = BurgerDirector(vegan_builder)
    burger2 = director.construct_burger()
    print("🥗 Vegan Burger:", burger2)
