'''
Created on Oct 30, 2017

@author: aleksandar.novic
'''
import random

# def guess(num):
#     while True:
#         if num != random.randrange(10):
#             print("Guess again looser")
#             
#         else:
#             print("U guessed it")
#             break
# 
# guessNum = int(input("Enter a number between 1 and 10: "))
# 
# guess(guessNum)

while True:
    guessNum = int(input("Enter a number between 1 and 10: "))
    if guessNum != random.randrange(10):
        print("Guess again looser")
    else:
        print("U guessed it!")
        break


