'''
Created on Oct 21, 2017

@author: aleksandar.novic
'''


# import random
# import math
# 
# randomList = ["string", 1.2345, 26]
# 
# oneToTen = list(range(10))
# 
# randomList = randomList + oneToTen
# 
# print(randomList[0])
# 
# print("List length: ", len(randomList))
# 
# first3 = randomList[0:3]
# 
# for i in first3:
#     print("{} : {}".format(first3.index(i), i))
# 
# print(first3[0]*3)
# 
# print("string" in first3)
# 
# print("Index of string: ", first3.index("string"))
# 
# print("how many string: ", first3.count("string"))
# 
# first3[0] = "new string"
# for i in first3:
#     print("{} : {}".format(first3.index(i), i))
# 
# first3.append("Another")
# 
# for i in first3:
#     print("{} : {}".format(first3.index(i), i))


import random
import math

#generate a random list of a random list, random values inside of the list, values btw 1 and 9

# numList = []
# 
# for i in range(5):
#     numList.append(random.randrange(1, 10))
# 
# for i in numList:
#     print(i)

#bubble sort

# numList = []
#  
# for i in range(5):
#     numList.append(random.randrange(1, 10))
# 
# i = len(numList) - 1
# 
# while i > 1:
#     j = 0
#     while j<i:
#         
#         print("\nIs {} > {}".format(numList[j], numList[j+1]))
#         
#         if numList[j] > numList[j + 1]:
#             
#             print("Switch")
#             
#             temp = numList[j]
#             numList[j] = numList[j+1]
#             numList[j+1] = temp
#         
#         else:
#             print("Dont switch")
#             
#         j = j+1
#         
#         for k in numList:
#             print(k, end=", ")
#         print()
#     
#     print("END OF ROUND")
#     
#     i = i-1
#     
# for k in numList:
#     print(k, end=", ")
# print()
'''
numList = []
  
for i in range(5):
    numList.append(random.randrange(1, 10))

numList.sort()

numList.reverse()

numList.insert(5, 10)

numList.remove(10)

numList.pop(2)
'''
#list comprehension, construct list in each item in the list

# numList = [1,2,3,4,5]
# 
# listOfValues = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)]
#                 for m in numList]
# 
# for i in listOfValues:
#     print(i)
# print()

# listTable = [[0]*4 for i in range(4)]
# 
# for i in range(4):
#     for j in range(4):
#         listTable[i][j] = "{} : {}".format(i, j)
# 
# for i in range(4):
#     for j in range(4):
#         print(listTable[i][j], end=" || ")
#     print()

'''
generate multiplication table
'''

#napravi listu
numList = [[0]*10 for i in range(10)]


#napravi for koji ce sam da appenduje brojeve u listu
for i in range(1, 10):
    for j in range(1, 10):
        numList[i][j] = i*j
        
        
        
#napravi for loop koji ce da svaki element mnozi u range od 1 do 10
for i in range(1, 10):
    for j in range(1, 10):
        print(numList[i][j], end=", ")
    print()




















