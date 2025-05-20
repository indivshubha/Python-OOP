class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} eats!")

    def sleep(self):
        print(f"{self.name} sleeps!")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Mouse(Animal):
    def speak(self):
        print("Squeak")

dog=Dog("Scooby")
cat=Cat("Garfield")
mouse=Mouse("Mickey")


dog.eat()
dog.sleep()
dog.speak()