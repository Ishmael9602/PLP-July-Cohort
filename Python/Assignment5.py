#  Assignment 1: Superhero Class with Encapsulation & Interface

class HeroAction:
    def perform_action(self):
        raise NotImplementedError("Subclasses must implement this method")

class Superhero(HeroAction):
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        return f"I am {self.name}, born in {self.origin}, and I wield the power of {self.power}!"

    def use_power(self):
        return f"{self.name} uses {self.power} to save the day!"

    def perform_action(self):
        return self.use_power()


# Activity 2: Polymorphism Challenge with move()

class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def move(self):
        return "Running "

class Bird(Animal):
    def move(self):
        return "Flying "

class Fish(Animal):
    def move(self):
        return "Swimming "


#  Test Function to Demonstrate Everything

def test_oop():
    print(" Superhero Demo:")
    hero = Superhero("Photon", "Light Manipulation", "Zion City")
    print(hero.introduce())
    print(hero.perform_action())

    print("\n Polymorphism Demo:")
    creatures = [Dog(), Bird(), Fish()]
    for creature in creatures:
        print(creature.move())

# Run the test
if __name__ == "__main__":
    test_oop()