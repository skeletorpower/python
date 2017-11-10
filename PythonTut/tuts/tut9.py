'''
Created on Oct 26, 2017

@author: aleksandar.novic
'''

'''
real world objects have attributes and capabilities 
in oop we will just DEFINE attrs and capas

so the attributes are called "fields" or "variables" 
and the capabilities called "methods" or "functions"

self refers as I refer to my things as my




'''
'''
class Dog:
    def __init__(self, name="", height = 0, weight = 0):
        self.name = name
        self.height = height
        self.weight = weight
        
    def run(self):
        print("{} the dog runs".format(self.name))

    def eat(self):
        print("{} the dog eats".format(self.name))
        
    def bark(self):
        print("{} the dog borks".format(self.name))


def main():
    spot = Dog("Spot", 66, 26)
    
    spot.bark()
    
    bowser = Dog()
    bowser.bark()
    
main()
'''
'''
class Square:
    def __init__(self, height="0",width = "0"):
        self.height = height
        self.width = width
    
    @property
    def height(self):
        print("Retrieving the height")
        
        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Not a number")


    @property
    def width(self):
        print("Retrieving the width")
        
        return self.__width

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Not a number")

    
    def getArea(self):
        return int(self.__width) * int(self.__height)


def main():
    aSquare = Square()
    
    height = input('Enter height: ')
    width = input('Enter width: ')
    
    aSquare.height = height
    aSquare.width = width
    
    print('Height: ', aSquare.height)
    print('Width: ', aSquare.width)
    
    print('The area is: ', aSquare.getArea())
    
main()
'''
import random
import math


class Warrior:
    def __init__(self, name="Warrior", health = 0, atkMax = 0, defMax = 0):
        self.name = name
        self.health = health
        self.atkMax = atkMax
        self.defMax = defMax
        
        
   
    def attack(self):
        atkMax = self.atkMax*(random.random()) + 0.5
        return atkMax
   
   
    def defence(self):
        defMax = self.defMax*(random.random()) + 0.5
        return defMax
   
class Battle:
    def fight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2)=="Game Over":
                print("Game Over")
                break     
   
            if self.getAttackResult(warrior2, warrior1)=="Game Over":
                print("Game Over")
                break  

    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAAtkAmt = warriorA.attack()
        warriorBBlockAmt = warriorB.defence()
        
        damage2WarrB = math.ceil(warriorAAtkAmt - warriorBBlockAmt)
        
        warriorB.health = warriorB.health - damage2WarrB
        
        print("{} attacks {} and deals {} damage".format(warriorA.name, warriorB, damage2WarrB))
        print("{} is down to {} health".format(warriorB.name, warriorB.health))
        if warriorB.health <= 0:
            print("{} has died".format(warriorB.name))
        else:
            return "fight again"
   
   
        
   


def main():
    
    maximus = Warrior("Maximus", 50, 20, 10)
    galaxon = Warrior("Galaxon", 50, 20, 10)
    
    battle = Battle()
    
    battle.fight(maximus, galaxon)
    
    
    
    
main()    




