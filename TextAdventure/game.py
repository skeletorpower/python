'''
Created on Nov 15, 2017

@author: aleksandar.novic
'''

import random
import textwrap
import sys
import os
import time
# import menu_screens

screen_width = 100



#### PLAYER SETUP ####
class Player:
    def __init__(self):
        self.name = ''
        self.hp = 0   
        self.mp = 0
        self.status_effectts = []
        self.location = 'start'
        self.gameOver = False
        self.speciality = ''
        
myplayer = Player()


#### DRAWING TITLE SCREEN ####
def titleScreenSelection():
    option = input('> ')
    
    if option.lower() == ('play'):
        setup_game()
        
    elif option.lower() == ('help'):
        helpMenu()
    
    elif option.lower() == ('quit'):
        sys.exit()

    while option.lower() not in ['play','help','quit']:
        print("Enter a valid command.")
        
        option = input('> ')
    
        if option.lower() == ('play'):
            setup_game()
            
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


    
### MAP ###    
    '''
     a1 a2 a3 a4
     -----------
    |  |  |  |  | a
    -------------
    |  |  |  |  | b
    -------------
    |  |  |  |  | c
    -------------
    |  |  |  |  | d
     -----------
    ''' 
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False
                 }

zoneMap = {
    'a1' : {
        ZONENAME : 'Town Market',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : '', 
        DOWN : 'b1',
        LEFT : '',
        RIGHT : 'a2',
            
        },
    'a2' : {
        ZONENAME : 'Town Gates',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : '',
        DOWN : 'b2',
        LEFT : 'a1',
        RIGHT : 'a3',
            
        },
    'a3' : {
        ZONENAME : 'Town Square',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : '',
        DOWN : 'b3',
        LEFT : 'a2',
        RIGHT : 'a4',
            
        },
    'a4' : {
        ZONENAME : 'Town Hall',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : '',
        DOWN : 'b4',
        LEFT : 'a3',
        RIGHT : '',
            
        },
    'b1' : {
        ZONENAME : 'B1',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'a1', 
        DOWN : 'c1',
        LEFT : '',
        RIGHT : 'b2',
            
        },
    'b2' : {
        ZONENAME : 'Home',
        DESCRIPTION : 'This is your home',
        EXAMINATION : 'It looks rather poorly decorated',
        SOLVED : False,
        UP : 'a2',
        DOWN : 'c2',
        LEFT : 'b1',
        RIGHT : 'b3',
            
        },
    'b3' : {
        ZONENAME : 'Graveyard',
        DESCRIPTION : 'A chills run down your spine as you see the number of graves that erect from the ground.',
        EXAMINATION : 'You can see a clear trail of wheels that passed right trough the center of the graveyard. Strange...',
        SOLVED : False,
        UP : 'a3',
        DOWN : 'c3',
        LEFT : 'b2',
        RIGHT : 'b4',
            
        },
    'b4' : {
        ZONENAME : 'B4',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'a4',
        DOWN : 'c4',
        LEFT : 'b3',
        RIGHT : '',
            
        },
    'c1' : {
        ZONENAME : 'C1',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'b1', 
        DOWN : 'd1',
        LEFT : '',
        RIGHT : 'c2',
            
        },
    'c2' : {
        ZONENAME : 'C2',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'b2',
        DOWN : 'd2',
        LEFT : 'c1',
        RIGHT : 'c3',
            
        },
    'c3' : {
        ZONENAME : 'C3',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'b3',
        DOWN : 'd3',
        LEFT : 'c2',
        RIGHT : 'c4',
            
        },
    'c4' : {
        ZONENAME : 'C4',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'b4',
        DOWN : 'd4',
        LEFT : 'c3',
        RIGHT : '',
            
        },
    'd1' : {
        ZONENAME : 'D1',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'c1', 
        DOWN : '',
        LEFT : '',
        RIGHT : 'd2',
            
        },
    'd2' : {
        ZONENAME : 'D2',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'c2',
        DOWN : '',
        LEFT : 'd1',
        RIGHT : 'd3',
            
        },
    'd3' : {
        ZONENAME : 'D3',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'c3',
        DOWN : '',
        LEFT : 'd2',
        RIGHT : 'd4',
            
        },
    'd4' : {
        ZONENAME : 'D4',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'c4',
        DOWN : '',
        LEFT : 'd3',
        RIGHT : '',
            
        }
    }    

    
    
#### GAME INTERACTIVITY ####    
def print_location():
    print('\n' + ('#' * (4 + len(myplayer.location))))    
    print('# ' + myplayer.location.upper() + ' #')
    print('# ' + zoneMap[myplayer.location][DESCRIPTION] + ' #')    
    print('\n' + ('#' * (4 + len(myplayer.location))))    
    
    
def prompt():
    print('\n' + '=============================')
    print('What would you like to do?')
    action = input('> ')
    acceptable_actions = ['move', 'go', 'travel', 'look', 'examine','interact', 'inspect', 'quit']
    
    while action.lower() not in acceptable_actions:
        print('Unknown action, try again.\n')
        action = input('> ')
    if action.lower() == 'quit':
        sys.exit()    
    elif action.lower() in ['move', 'go', 'travel']:
        player_move(action.lower())
    elif action.lower() in ['look', 'examine', 'inspect']:
        player_examine(action.lower())    
    elif action.lower() in ['interact']:
        player_interact(action.lower())
        

def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask)    
    
    if dest in ['up', 'north']:
        destination = zoneMap[myplayer.location][UP]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zoneMap[myplayer.location][DOWN]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zoneMap[myplayer.location][LEFT]
        movement_handler(destination)     
    elif dest in ['right', 'east']:
        destination = zoneMap[myplayer.location][RIGHT]
        movement_handler(destination)
        

def movement_handler(destination):
    print('\n' + "You have moved to the " + destination + '.')
    destination = myplayer.location
    print_location()


def player_examine(action):
    if zoneMap[myplayer.location][SOLVED]:
        print('You have already exhausted this zone.')
    else:
        print('You can trigger puzzle here')


def player_interact(someObj):
    pass





        
#### GAME FUNCTIONALITY ####
def startGame():
    return
    

def main_game_loop():
    while myplayer.gameOver is False:
        prompt()
    #handle puzzles bosses etc
    

    
def setup_game():    
    os.system('clear')
    
    ### NAME COLLECTING ###
    question1 = 'Hello, who are you?\n'
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input('> ')
    myplayer.name = player_name
    
    
    ### SPELL SWORD HANDLING ###
    question2 = 'So, are you a spellcaster or a swordsman?\n'
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_speciality = input('> ')
    myplayer.speciality = player_speciality
    
    
    ### STATISTICS ###
    if player_speciality in ['spellcaster', 'swordsman']:
        if player_speciality.lower() is 'swordsman':
            myplayer.hp = 100
            myplayer.mp = 0
        elif player_speciality.lower() is 'spellcaster':
            myplayer.hp = 60
            myplayer.mp = 150
    while player_speciality not in ['spellcaster', 'swordsman']:
        player_speciality = input('> ')
        myplayer.speciality = player_speciality
        if player_speciality in ['spellcaster', 'swordsman']:
            if player_speciality.lower() is 'swordsman':
                myplayer.hp = 100
                myplayer.mp = 0
            elif player_speciality.lower() is 'spellcaster':
                myplayer.hp = 60
                myplayer.mp = 150
    
    
    ### INTRODUCTION ###
    
    
    if player_speciality is 'swordsman':
        print('Well, I have a special task for you!')
        speech = '''The word is that some nasty bandits just inhabited our precious trade roads\n
                    and it would be shame if some innocent fold lose their lives 'cuz of these rodents.\n
                    Will you be kind enough to go and investigate the road south from here? I will reward you!'''
        for character in speech:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.03)
        
    elif player_speciality is 'spellcaster':
        print('Well, I have a special task for you!')
        speech = '''The word is that some nasty ghouls rose up from their graves and now seek food\n
                    outside of the graveyard. Will you go investigate?'''
        for character in speech:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.03)
    
    os.system('clear')
    print('########################')
    print('# Your journey begins! #')
    print('########################')
    
    main_game_loop()
    
    
    
    
    
    
    
    
    
titleScreen()

    
    
    
    
    

