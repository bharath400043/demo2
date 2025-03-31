from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self):
        pass
    def eating(self):
        print("Have eating behaviour")
    def sleeping(self):
        print("Have sleep behaviour")
    @abstractmethod
    def running(self):
        pass
class Cat(Animal):
    def __init__(self):
        pass
    def running(self):
        print("Cat has running behaviour")

class Dog(Animal):
    def __init__(self):
        pass
    def running(self):
        print("Dog has running behaviour")

snoopy = Dog()
snoopy.running()
snoopy.eating()