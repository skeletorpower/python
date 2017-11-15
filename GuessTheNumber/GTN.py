'''
Created on Nov 14, 2017

@author: aleksandar.novic
'''

import random

while True:
    guessNum = int(input("Enter num between 1 and 5: "))
    secretNum = random.randint(1,5)
    
    if guessNum == secretNum:
        print("You won!")
        break
    else:
        print("Try again! ")

















