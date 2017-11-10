'''
Created on Oct 17, 2017

@author: aleksandar.novic
'''

# STRING FUNCTIONS

# randomString = "     this is some string    "
# 
# randomString = randomString.lstrip()
# 
# randomString = randomString.rstrip()
# 
# randomString = randomString.strip()
# 
# print(randomString.capitalize())
# 
# print(randomString.upper())
# 
# print(randomString.lower())
# 
# someList = ["Bunch", "of", "random", "words"]
# 
# print(" ".join(someList))
# 
# someList2 = randomString.split()
# for i in someList2:
#     print(i)
# print("How many: ", randomString.count("is"))
# 
# print("Where is string: ", randomString.find("string"))
# 
# print(randomString.replace("an", "a kind of"))

#-----------------------------------------------------------
#acronim problem
# 
# sentence = input("Convert to Acronym: ")
# 
# acronym = ""
# 
# for i in sentence.upper().split():
#     acronym = acronym + i[0]
# print(acronym)

#-------------------------------------------------------------

# letter_z = "z"
# num_3 = "3.14"
# a_space = " "
# 
# print("is z a letter or number ", letter_z.isalnum())
# 
# print("is z a letter ", letter_z.isalpha())
# 
# print("is 3 a number ", num_3.isdigit())
# 
# print("is 3 a letter ", num_3.isalpha())
# 
# print("is z an uppercase", letter_z.isupper())
# 
# print("is z a lowercase ", letter_z.islower())
# 
# 
# def isFloat(str_val):
#     try:
#         float(str_val)
#         return True
#     except ValueError:
#         return False
# 
# print("is PI a float: ", isFloat(num_3))

#a problem, encripting messages

message = input("Enter something here ")

key = int(input("How many characters to shift (1-26)"))

secretMSG = ""

for char in message:
    if char.isalpha():
        charCode = ord(char)
        charCode = charCode + key
        
        if char.isupper():
            if charCode > ord("Z"):
                charCode = charCode - 26
            if charCode < ord("A"):
                charCode = charCode + 26
             
        else:
            
            if charCode > ord("z"):
                charCode = charCode - 26
            if charCode < ord("a"):
                charCode = charCode + 26

        secretMSG = secretMSG + chr(charCode)
    else:
        secretMSG = secretMSG + char
        
print("Encrypted: ", secretMSG)

key = -key

originalMSG = ""

for char in secretMSG:
    if char.isalpha():
        charCode = ord(char)
        charCode = charCode + key
        
        if char.isupper():
            if charCode > ord("Z"):
                charCode = charCode - 26
            if charCode < ord("A"):
                charCode = charCode + 26
             
        else:
            
            if charCode > ord("z"):
                charCode = charCode - 26
            if charCode < ord("a"):
                charCode = charCode + 26

        originalMSG = originalMSG + chr(charCode)
    else:
        originalMSG = originalMSG + char
        
print("Decrypted: ", originalMSG)
