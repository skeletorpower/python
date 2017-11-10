'''
Created on Nov 9, 2017

@author: aleksandar.novic
'''

from d4Die import rollD4
from d6Die import rollD6
from d8Die import rollD8
from d10Die import rollD10
from d12Die import rollD12
from d20Die import rollD20
from d100Die import rollD100


def diceSelection():
    
    selection = input("Choose one of the official D&D dice: ")
    
    if selection == 'd4':
        print("You rolled {} on a {}!".format(rollD4(), selection))

    elif selection == 'd6':
        print("You rolled {} on a {}!".format(rollD6(), selection))
        
    elif selection == 'd8':
        print("You rolled {} on a {}!".format(rollD8(), selection))
        
    elif selection == 'd10':
        print("You rolled {} on a {}!".format(rollD10(), selection))
        
    elif selection == 'd12':
        print("You rolled {} on a {}!".format(rollD12(), selection))
        
    elif selection == 'd20':
        print("You rolled {} on a {}!".format(rollD20(), selection))
        
    elif selection == 'd100':
        print("You rolled {} on a {}!".format(rollD100(), selection))
        
    else:
        print("You need to choose one of official D&D dice which includes" + "\n" + "d4, d6, d8, d10, d12, d20, d100")    


def main():
    
    
    while True:
        diceSelection()
        
        again = input("Roll again? ")
        if again == 'n':
            break
        
      

main()