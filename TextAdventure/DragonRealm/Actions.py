'''
Created on Nov 17, 2017

@author: aleksandar.novic
'''
import sys
import time


actions = ['hide', 'run', 'move', 'look', 'listen', 'quit']
closeActions = ['examine', 'interact', 'inspect']

def run():
    narator = "\nYou try to run away"
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

def move(str):
    narator = "You moved {}".format(str)
    for c in narator:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def look():
    narator = "You look around"
    for c in narator:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
    
def examine(str):
    narator = "You examined {}".format(str)
    for c in narator:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)    

def interact(str):
    narator = "You interact with {}".format(str)
    for c in narator:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def inspect(str):
    narator = "You inspected the {}".format(str)
    for c in narator:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def quit():
    sys.exit()
    
