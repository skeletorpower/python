'''
Created on Nov 20, 2017

@author: aleksandar.novic
'''

import sys
import time

def narrate(str):
    for c in str:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
    
    print(str)

