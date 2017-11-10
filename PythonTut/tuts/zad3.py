'''
Created on Oct 30, 2017

@author: aleksandar.novic
'''
from builtins import property

# class Dog:
#     def __init__(self, name="", height="", weight=""):
#         self.name = name
#         self.heigh =height
#         self.weight = weight
#         
#     def run(self):
#         print("{} the dog runs".format(self.name))
# 
#     
#     def eat(self):
#         print("{} the dog eats".format(self.name))    
# 
# 
# 
# def main():
#     spot = Dog("Spot")
#     
#     spot.eat()
#     
#     bowser = Dog()
#     bowser.name = "Bowser"
#     bowser.run()
# 
# main()
'''
class Square:
    def __init__(self, height="0", width="0"):
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
            print("Enter numbers only")

    @property
    def width(self):
        print("Retrieving the width")
        return self.__width


    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Enter numbers only")




    def getArea(self):
        return int(self.__width) * int(self.__height)
    

def main():
    aSquare = Square()
    height = input("Enter height: ")
    width = input("Enter width: ")
    
    aSquare.height = height
    aSquare.width = width
    
    print("Height: ", aSquare.height)
    print("width: ", aSquare.width)
    
    print("The area is: ", aSquare.getArea())
    
main()
'''

'''
import random

class Warrior:
    def __init__(self, name="", health = 0, attackDmg = 0, blockDmg = 0):
        self.name = name
        self.health = health
        self.attackDmg = attackDmg
        self.blockDmg = blockDmg
        
    def attack(self):
        atkAmt = self.attackDmg
        return atkAmt
    
    
    def block(self):
        blkAmt = self.blockDmg
        return blkAmt
    


class Battle:
    def startFight(self, warrior1, warrior2):
        while True:
            if self.getAtkResult(warrior1, warrior2) == "Game Over":
                print("Game over")
                break
           
            if self.getAtkResult(warrior2, warrior1) == "Game Over":
                print("Game over")
                break
                
    
    @staticmethod
    def getAtkResult(warriorA, warriorB):
        
        warriorAAtkAmt = warriorA.attack()
        
        warriorBBlkAmt = warriorB.block()
    
        damage2WarB = warriorAAtkAmt - warriorBBlkAmt
    
        warriorB.health = warriorB.health - damage2WarB
    
        print("{} attacks {} and deals {} damage".format(warriorA.name, warriorB.name, damage2WarB))
        print("{} is down to {} health".format(warriorB.name, warriorB.health))
    
        
        if warriorB.health <= 0:
            print("{} has died and {} is victorious".format(warriorB.name, warriorA.name))
            return "Game Over"
        else:
            return "Fight again"

        
def main():

    galaxon = Warrior("Galaxon", 30, random.randrange(15), 0)
    maximus = Warrior("Maximus", 26, random.randrange(12), 0)

    battle = Battle()

    battle.startFight(galaxon, maximus)


main()
'''







































