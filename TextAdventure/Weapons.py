'''
Created on Nov 17, 2017

@author: aleksandar.novic
'''

import Damage
import random

def longswordDamage():
    lsDmg = Damage.d8
    return lsDmg


def severalD6(num):
#     num = int(input("how many d6? "))
    dmgsum = [Damage.d6 for x in range(num)]
    
    return sum(x, dmgsum)

print(severalD6(int(input("how many d6 "))))




















