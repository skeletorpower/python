'''
Created on Nov 9, 2017

@author: aleksandar.novic
'''
from random import randint
'''
attack = {'quick': (lambda: print("Quick attack")),
          'power': (lambda: print("Power attack")),
          'miss': (lambda: print("Missed attack"))}

# attack['quick']()


import random

attackKey = random.choice(list(attack.keys()))

attack[attackKey]()
'''

#random flip coin problem
'''
import random

flips = []

for i in range(1,101):
    flips+= random.choice(['h','t'])

print("Heads", flips.count('h'))
print("Tails", flips.count('t'))
'''

'''
import random

thousandList = list(randint(1,1001) for i in range(100))

print(list(filter((lambda x: x % 9 == 0), thousandList)))
'''













