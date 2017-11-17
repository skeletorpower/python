'''
Created on Nov 17, 2017

@author: aleksandar.novic
'''
import sys
import time


actions = ['hide', 'run', 'move', 'look', 'quit']
closeActions = ['examine', 'interact', 'inspect']

def run():
    narator = "You try to run away."
    for c in narator:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def hide():
    narator = "You quickly look around for a good place to hide..."
    for c in narator:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def move(position):
    narator = "You moved {}".format(position)
    for c in narator:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def look():
    narator = "You look around "
    for c in narator:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
    
def examine(obj):
    narator = "You examined {}".format(obj)
    for c in narator:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)    

def interact(obj):
    narator = "You interact with {}".format(obj)
    for c in narator:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def inspect(obj):
    narator = "You inspected the {}".format(obj)
    for c in narator:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def quit():
    sys.exit()
    
