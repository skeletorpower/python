'''
Created on Nov 15, 2017

@author: aleksandar.novic
'''


import sys
import os


def titleScreenSelection():
    option = input('> ')
    
    if option.lower() == ('play'):
        startGame()
        
    elif option.lower() == ('help'):
        helpMenu()
    
    elif option.lower() == ('quit'):
        sys.exit()

    while option.lower() not in ['play','help','quit']:
        print("Enter a valid command.")
        
        option = input('> ')
    
        if option.lower() == ('play'):
            startGame()
            
        elif option.lower() == ('help'):
            helpMenu()
        
        elif option.lower() == ('quit'):
            sys.exit()


def titleScreen():
    os.system('clear')
    print('################################')
    print('#         Text dungeon         #')
    print('################################')
    print('#           - Play -           #')
    print('#           - Help -           #')
    print('#           - Quit -           #')
    print('################################')
    print()
    print(' Copyright 2017 Aleksandar Novic')
    
    titleScreenSelection()

def helpMenu():
    print('########################################')
    print('#          Text dungeon help           #')
    print('########################################')
    print('  - Use up, down, left, right to move - ')
    print(' - Type your commands to execute them - ')
    print('       - Use look to inspect -          ')
    print('########################################')
    
    titleScreenSelection()


def startGame():
    
























