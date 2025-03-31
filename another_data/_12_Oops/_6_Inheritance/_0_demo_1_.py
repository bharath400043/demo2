
def get_data():
    pass


"""
                              Animal
                DomesticAnimal        WildAnimal
                  Cat    Dog              Tiger Lion


                           Animal
                  Cat    Dog   Tiger    Lion


SoftwareEmployee   GovtEmployee   BankEmployee
     update_hike(rating)    update_hike()   update_hike()



"""
''''
             Employee
     PvtEmployee   GvtEmployee

'''









class Animal:
    def __init__(self):
        pass

class Cat:
    def __init__(self):
        pass
    def eating(self):
        print("Eating")

class Dog:
    def __init__(self):
        pass
    def eating(self):
        print("Eating")

class Tiger:
    def __init__(self):
        pass
    def eating(self):
        print("Eating")

    def running(self):
        print("Tiger running")
class Lion():
    def __init__(self):
        pass
    def eating(self):
        print("Eating")

    def running(self):
        print("Lion running")
'''
cat = Animal()
dog = Animal()
tiger = Animal()
lion = Animal()
'''
cat = Cat()
dog = Dog()
tiger = Tiger()
lion = Lion()

'''
XX ==> Only Super class : Animal,Employee : Unnecessarily other behavior also will come to our object

XX ==> Only Sub classes : Code duplication. For example one method is common for all classes,then code duplication will happen

Solution : Use Inheritance 
           Implement classes as Super class - Sub class mechansim
'''

class Animal:
    def __init__(self):  # Common state
        print("In Animal object")
    # Generic behavior
    def eating(self):   # Common behavior for all sub classes
        print("Animal Eating")

class Cat(Animal):  # Cat is-a Animal

    def __init__(self):
        print("In CAT object")
    # Specific behavior
    def sleeping(self):
        print("Cat is sleeping")

animal = Animal()
animal.eating()

# animal.sleeping()
print("-----------------")

cat = Cat()
cat.sleeping()
cat.eating()
'''
Here Cat is sub class and Animal is super class. Cat as a sub class wil inherit all the features of Animal
Inheritance should be applicable when IS-A *** relationship is satisfied

'''

# Method overriding ==> Dynamic polymorphism
