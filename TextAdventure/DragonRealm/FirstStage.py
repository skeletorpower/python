'''
Created on Nov 20, 2017

@author: aleksandar.novic
'''

import Actions
import sys
import time
import textwrap


def start_game():
    narrate = '''As you came out from hiding, and your roofless house, you can see that Honeyberg, your village,
is destroyed. Many houses burned to the ground, others crumbled. You think you hear some people down the street.
What will you do? Look/Listen/Move'''
    for c in narrate:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
    
    while True:
        action = input('> ')
        if action in Actions.actions:
            if action == 'look':
                Actions.look()
                narrate = ", you see destroyed village, big footsteps and a dead soldier."
                for c in narrate:
                    sys.stdout.write(c)
                    sys.stdout.flush()
                    time.sleep(0.01)
                print("What will you do? Examine soldier/Move away")
                
                while True:
                    action = input('> ')
                    if action in Actions.closeActions:
                        if action == 'examine':
                            Actions.examine("soldier")
                            
    
    
    
    
    
    
    