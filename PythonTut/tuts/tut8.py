'''
Created on Oct 25, 2017

@author: aleksandar.novic
'''
from idlelib.iomenu import encoding
'''
import os
from idlelib.iomenu import encoding

with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore random text\nAnd some more")

with open("mydata.txt", encoding="utf-8") as myFile:
    print(myFile.read())
     
os.rename("mydata.txt", "mydata2.txt")
os.remove("mydata2.txt")

# os.mkdir("mydir")
os.chdir("mydir")

print("current directory ", os.getcwd())
os.chdir("..")
print("current directory ", os.getcwd())

os.rmdir("mydir")
'''

'''
import os
def fibonaci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    
    else:
        return fibonaci(num-1) + fibonaci(num-2)

ask = int(input("How many numers: "))

for i in range(ask):
    print(fibonaci(i))

print("All done")
'''
'''
import os

words = []
with open("mydata2.txt", encoding="utf-8") as myFile:
    
    lineNum = 1
    
    while True:
        line = myFile.readline()
        if not line:
            break
        
        print("line", lineNum)
        
        wordList = line.split()
        
        print("Number of words", len(wordList))
        
        charCount = 0
        
        for word in wordList:
            for char in word:
                charCount +=1
        
        avgNumChars = charCount/len(wordList)
        
        print("Avg word length : {:.2}".format(avgNumChars))
        
        lineNum +=1
  '''  
    
#tuples

myTuple = (1,2,3,4,5,6)

print("1st Value: ", myTuple[0])









