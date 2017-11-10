'''
Created on Oct 16, 2017

@author: aleksandar.novic
'''

#exception handling

# while True:
#     try:
#         number = int(input('Please enter a number: '))
#         break
# 
#     except ValueError:
#         print("You cheeky bastard")
#     
#     except:
#         print("An unknown shit happened")
#         
# print("Thank you")
# 

#problem 1, do while



number = 7

while True:
    guess = int(input("Enter a number: "))
    
    if guess == number:
        print("U FKIN WON")
        break
    else:
        print("Try AGAIN MOFO")
        



















