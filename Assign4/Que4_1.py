from abc import ABC, abstractmethod


# Base Abstract Class
class Animal(ABC):
    def __init__(self,  group, color):
        self.mygroup = group
        self._mycolor = color                  
             
        print("My tone is",self._mycolor,"in colour")
       
    # common method
    def isgroup(self):
        print("I belong to the group of", self.mygroup)  # group refers to mammals, reptiles, birds

    # Abstract method
    @abstractmethod
    def sounds(self):
        print(" I can make sounds")

#base classes and derived classes form a hierarchy
#Polymorpism is shown by function class Animal, where init has overriding functionality


#Derived classes
class Dog(Animal):   #mammal
    def isgroup(self):
        print("I belong to the group of", self.mygroup)

    #implementation of abstract methods
    def sounds(self):
        print("I Bark")

class Cat(Animal):    #mammal
    def isgroup(self):
        print("I belong to the group of", self.mygroup)

    def sounds(self):
        print("I mew")


#Interfaces has implicitly only abstract method as followed 
class Bear(Animal):
    

    def sounds(self):
        print("I growl")

class Giraffes(Animal):
    def isgroup(self):
        print("I belong to the group of", self.mygroup)

    def sounds(self):
        print("I bleat")


class Lizard(Animal):       #reptiles, carnivores
    def isgroup(self):
        print("I belong to the group of", self.mygroup)

    def sounds(self):
        print("I squeak")


class Crows(Animal):       #birds , omnivores
    def isgroup(self):
        print("I belong to the group of", self.mygroup)

    def sounds(self):
        print("I Caw")


class Lion(Animal):
    def isgroup(self):
        print("I belong to the group of", self.mygroup)

    def sounds(self):
        print("I roar")


class Grasshopper(Animal):  #insect
    def isgroup(self):
        print("I belong to the group of", self.mygroup)

    def sounds(self):
        print("I chirp")

class Frogs(Animal):
    def isgroup(self):
        print("I belong to the group of", self.mygroup)

    def sounds(self):
        print("I croak")




x = Frogs("Amphibian","green ")
x.sounds()


