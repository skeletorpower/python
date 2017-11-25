'''
Created on Nov 17, 2017

@author: aleksandar.novic
'''
import random
import textwrap
import time
import sys
import Actions
import MainMenu
from Narrator import narrate

def hideFromThreat():
    narrate('''\nYou hear big and slow footsteps approaching. Next thing you know, you don't have\n
roof on that cute little house of yours. You hear something very big breathing loudly for a few\n
moments, then, silence.
''')

def lookAfterHiding():
    narrate('''\nAfter you get out from hiding you can clearly see that you don't have roof no more.\n
Only things you can see is the big giant's back, and the teal colored sky above.
Truly a sad day for you.
''')


def displayIntro():
    narator = '''\nYou find yourself in your lovely home. \nYou just added some finishing touches for the new decoration of the kitchen. It looks perfect.
As you sit to eat on your newly painted chair you suddenly hear thunderous noise outside.
People screaming, and the floor shaking.
What will you do?
Look/Hide
    
'''
    for c in narator:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
    
    while True:
        action = input('> ')
        if action.lower() not in Actions.actions:
            print('Unknown action, enter some of these: ', Actions.actions)
    
        if action.lower() == 'quit':
            Actions.quit()
        elif action.lower() == 'hide':
            Actions.hide()
            print("You can see 3 places. Bed, table and wardrobe.")
            print("Where will you hide?")
            while True:
                actionHide = input('> ')
                options = ['bed', 'table', 'wardrobe']
                if actionHide.lower() not in options:
                    print('Choose one of these options: ', options)
            
                if actionHide.lower() == 'bed':
                    print('You hid yourself under the bed in hope of survival')
                if actionHide.lower() == 'wardrobe':
                    print('You hid yourself inside of rather large wardrobe in hope of survival')
                if actionHide.lower() == 'table':
                    print('You hid yourself under the table. Tablecloth is obscuring you.')
                    
                hideFromThreat()
                print("What will you do?")
                while True:
                    action = input('> ')
                    if action.lower() not in Actions.actions:
                        print('Unknown action, enter some of these: ', Actions.actions)
                    if action.lower() != 'hide':
                        if action.lower() == 'look':
                            lookAfterHiding()
                            narrate = "'This is going to be a great adventure' you think at least...."
                            for c in narrate:
                                sys.stdout.write(c)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(narrate)
                            print("")
                            MainMenu.displayMainMenu()
            
        
        elif action.lower() == 'look':
            Actions.look()
            narrate = '''You fasted toward the window to see what is happening.
Apparently, handful of hill giants attacked the village, you can see one coming right at your house.
What will you do?   Hide/Run'''   
            for c in narrate:
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(0.01)     
            
            while True:
                action = input('> ')
                options = ['hide', 'run']
                if action.lower() == 'hide':
                    Actions.hide()
                    print("You can see 3 places. Bed, table and wardrobe.")
                    print("Where will you hide?")
                    while True:
                        actionHide = input('> ')
                        options = ['bed', 'table', 'wardrobe']
                        if actionHide.lower() not in options:
                            print('Choose one of these options: ', options)
                    
                        if actionHide.lower() == 'bed':
                            print('You hid yourself under the bed in hope of survival')
                        if actionHide.lower() == 'wardrobe':
                            print('You hid yourself inside of rather large wardrobe in hope of survival')
                        if actionHide.lower() == 'table':
                            print('You hid yourself under the table. Tablecloth is obscuring you.')
                
                        hideFromThreat()
                        print("What will you do?   Move/Look/Inspect/Examine")
                        while True:
                            action = input('> ')
                            if action.lower() not in Actions.actions:
                                print('Unknown action, enter some of these: ', Actions.actions)
                            if action.lower() != 'hide':
                                if action.lower() in ['look', 'examine', 'inspect', 'move']:
                                    lookAfterHiding()
                                    narrate = "'This is going to be a great adventure' you think at least..."
                                    for c in narrate:
                                        sys.stdout.write(c)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    print(narrate)
                                    print("")
                                    MainMenu.displayMainMenu()
                
                if action.lower() == 'run':
                    Actions.run()
                    narrate = ''', unfortunately the giant sees you and lashes his hand to grab you. He succeeds
and smashes your body with his hand. Next thing you know, you are in smelly giant's bag full of
unfortunate souls like yourself. Your fate is sealed.
'''
                    for c in narrate:
                        sys.stdout.write(c)
                        sys.stdout.flush()
                        time.sleep(0.02)
                    MainMenu.gameOver()
                    
                
                
                
                
                
                
                
            
displayIntro()





















