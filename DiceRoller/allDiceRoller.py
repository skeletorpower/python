'''
Created on Nov 9, 2017

@author: aleksandar.novic
'''

import random

def rollD6():
    return random.randrange(1, 7)
# rollD6()
# 
def rollD4():
    return random.randrange(1, 5)
# rollD4()
# 
def rollD8():
    return random.randrange(1, 9)
# rollD8()
# 
def rollD10():
    return random.randrange(1, 11)
# rollD10()
# 
def rollD12():
    return random.randrange(1, 13)
# rollD12()
# 
def rollD20():
    return random.randrange(1, 21)
# rollD20()
# 
def rollD100():
    return random.randrange(1, 101)
# rollD100()
# 
while True:
    selection = input("Choose a D&D dice: ")
#     options = {
#         'd4' : rollD4(),
#         'd6' : rollD6(),
#         'd8' : rollD8(),
#         'd10' : rollD10(),
#         'd12' : rollD12(),
#         'd20' : rollD20(),
#         'd100' : rollD100()
#     }
    
    if selection == 'd4':
        print("Rolled {} on {}! ".format(rollD4(), selection))
         
    elif selection == 'd6':
        print("Rolled {} on {}! ".format(rollD6(), selection))
        
    elif selection == 'd8':
        print("Rolled {} on {}! ".format(rollD8(), selection))
        
    elif selection == 'd10':
        print("Rolled {} on {}! ".format(rollD10(), selection))
        
    elif selection == 'd12':
        print("Rolled {} on {}! ".format(rollD12(), selection))
        
    elif selection == 'd20':
        print("Rolled {} on {}! ".format(rollD20(), selection))
        
    elif selection == 'd100':
        print("Rolled {} on {}! ".format(rollD100(), selection))
    
    else:
        print("You need to choose one of official D&D dice which includes" + "\n" + "d4, d6, d8, d10, d12, d20, d100")    
        
    again = input("Roll again? y/n ")
    
    if again == 'n':
        break
        
        
