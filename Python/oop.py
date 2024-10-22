from datetime import date
from math import pi

class Person:

    # constructor of the class
    def __init__(self, name, age):

        self.__name = name
        self.__age = age

    def display(self):
        return f"My name is {self.__name} and my age is {self.__age}"
    

    def aging (self, num):
        if self.__age <= num:
            print("old")
        else:
            print("Young")
    #instance methods
    #incabsulation
    def get_name(self):
        return self.__name
    
    def set_name (self, nam):
        self.__name = nam

    def get_age(self):
        return self.__age
    
    def set_age(self, ag):
        self.__name = ag

    @classmethod 
    def initFrombirthYear(cls, name, birthYear, extra) :
        return cls(name, date.today().year - birthYear, extra) 
    
    # add two object parameters
    def __add__(self, other):
        names = self.__name + " and " + other.__name
        ages = self.__age + other.__age
        return f"names are {names} and ages are {ages}"
    
    def __lt__(self, other):
        return self.__age < other.__age

#inheritance
class Man(Person):
    gender = "Male"
    count = 0
    def __init__(self, name, age, voice):
        super().__init__(name, age)   
        self.voice = voice
        Man.count+=1
# polyMorphism
    def display(self):
        str =  super().display()
        return str + f", my voice is {self.voice} and my gender is {self.gender}"



class Pizza:

    def __init__(self, r, ingred):
        self.ingred = ingred
        self.r = r

    @classmethod
    def veg(cls):
        return cls(15, ['mushrom', 'olives', 'onions'])
    
    # class methods
    # Need to take the class as a parameter
    # can change the class state or attributes
    @classmethod
    def marg(cls):
        return cls(20, ['mozarilla', 'sauce'])
    
    def __str__(self):
        return f"Pizza ingredients are {self.ingred}"
    
    @staticmethod
    def circle(rad):
        return rad*rad*pi
    
    def area(self):
        return Pizza.circle(self.r)



# staic Methods
#does not take self or any parameters from the class
class Math:
    @staticmethod
    def add(x, y):
        return x + y
    @staticmethod
    def add5(num):
        return num + 5
    @staticmethod
    def add10(num):
        return num + 10 


class Dates:
    def __init__(self, __date):
        self.__date = __date

    def get_Date(self):
        return self.__date
    
    def setDate(self, daten):
        self.__date = daten
    
    @staticmethod
    def toDash(date):
        return date.replace("/", "-") 
        
x1 = Math.add(10, 16)
print(x1) 
pizza5 = Pizza(6, ['onion', 'tomato'])
print(pizza5.area())

date1 = Dates("12-12-2012")
date2 = "12/12/2012"
datea = Dates.toDash(date2)
if(date1.get_Date() == datea):
    print("Equal")


man = Man("ali", 25, "hard")
man2 = Man("alia", 30, "soft")
print(man.display())
man2 = Man.initFrombirthYear("Islam", 2004, "hard")

print(man2.display())
print(isinstance(man2, Man))
print(isinstance(man2, Person))

man3 = Person("ali", 25)
man4 = Person("alia", 30)
print(man3 + man4)

print(man3 < man4)


# abstraction
from abc import ABC, abstractmethod

class shape(ABC):

    @abstractmethod
    def parametr(self):
        pass

    @abstractmethod
    def area(self):
        pass

#inheritance of the abstract class

class circle(shape):

    def __init__(self, __radius):
        self.__radius = __radius

    def area(self):
        return self.__radius * self.__radius *pi
    
class rect(shape):
    def __init__(self, __w, __h) -> None:
        self.__h = __h
        self.__w = __w
    
    def area(self):
        return self.__w * self.__h
    
    def parametr(self):
        return (self.__w + self.__h)*2
    
rect = rect(5, 6).area()
print(rect)

        
    

