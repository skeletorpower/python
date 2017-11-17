'''
Created on Nov 17, 2017

@author: aleksandar.novic
'''

import sys
import os





def titleScreenSelection():
    while True:
        option = input('> ')
        options = ['play','help','quit']
        if option.lower() == ('play'):
#             start_game()
            pass
        elif option.lower() == ('help'):
            helpMenu()
        
        elif option.lower() == ('quit'):
            sys.exit()
        
        else:
            print("Select something from these options: ", options)


def displayMainMenu():
#     os.system('cls' if os.name == 'nt' else 'clear')
    print('                ################################')
    print('                #         Text dungeon         #')
    print('                ################################')
    print('                #           - Play -           #')
    print('                #           - Help -           #')
    print('                #           - Quit -           #')
    print('                ################################')
    print()
    print(' Copyright 2017 Aleksandar Novic')
    
    titleScreenSelection()

def helpMenu():
    print('########################################################################')
    print('#                          Text dungeon help                           #')
    print('########################################################################')
    print("  - type 'hide', 'run', 'move', 'look' to interact with environment - ")
    print(" - type 'examine', 'interact', 'inspect' to interact with an object -")
    print('                               - enjoy :) -                          ')
    print('#########################################################################')
    
    titleScreenSelection()