

class Animal:
    alive=True

class Dog(Animal):
    def speak(self):
        print("Woof")

class Car:
    alive=False
    def speak(self):
        print("Honk")

class Cat(Animal):
    def speak(self):
        print("Meow")

animals=[Dog(),Cat(),Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)