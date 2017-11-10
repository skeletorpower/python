'''
Created on Oct 16, 2017

@author: aleksandar.novic
'''

# for i in range(1, 21):
#     if i%2 != 0:
#         print(i)


# investment = float(input("Enter your investment: "))
# 
# interest = float(input("Enter your interest: ")) * .01
# 
# 
# for i in range(11):
#     investment = investment+(investment*interest)
#     print("Your earnings for {} year is: {:.2f}".format(i, investment) )


height = int(input("How tall is the tree: "))

spaces = height -1

hashes = 1

stump = spaces


while height != 0:
    for i in range(spaces):
        print(" ", end="")
    for i in range(hashes):
        print("#", end="")
    print()
    
    spaces-=1
    hashes+=2
    height -=1
    
for i in range(stump):
    print(" ", end="")
print("#")






