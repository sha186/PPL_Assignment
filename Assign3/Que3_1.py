from abc import ABC, abstractmethod


# Base Abstract Class
class Animal(ABC):
    def __init__(self, color, eatinghabit):
        
        self._mycolor = color                  #protected variable
        self.__myeatinghabit = eatinghabit     #private variable
        print("My tone is",self._mycolor,"in colour")
        print("I am",self.__myeatinghabit, "by food habit")


    
    # Abstract method
    @abstractmethod
    def sounds(self):
        print(" I can make sounds")


#Derived classess
class Dog(Animal):   #mammal
   

    #implementation of abstract methods
    def sounds(self):
        print("I Bark")

class Cat(Animal):    #mammal
    
    def sounds(self):
        print("I mew")

class Bear(Animal):
   
    def sounds(self):
        print("I growl")

class Giraffes(Animal):
    

    def sounds(self):
        print("I bleat")


class Lizard(Animal):       #reptiles, carnivores
   
    def sounds(self):
        print("I squeak")


class Crows(Animal):       #birds , omnivores
   
    def sounds(self):
        print("I Caw")


class Lion(Animal):
   
    def sounds(self):
        print("I roar")


class Grasshopper(Animal):  #insect
    

    def sounds(self):
        print("I chirp")

class Frogs(Animal):
    
    def sounds(self):
        print("I croak")




x = Frogs("green ","carnivore")
x.sounds()


