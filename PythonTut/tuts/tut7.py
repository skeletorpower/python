'''
Created on Oct 22, 2017

@author: aleksandar.novic
'''
#create dictionary
'''
acaDict = {"fName": "Aca", "lName": "Novic"}
#pull data by key
print("My name: ", acaDict["fName"])
#change value by key
acaDict["fName"] = "Aleksandar"
print(acaDict)
#add new k v pair
acaDict["city"] = "Indjija"
#check if key exists
print("Is there a city: ", "city" in acaDict)

#get a list of values
print(acaDict.values())
#get a list of keys
print(acaDict.keys())
#get both
for k, v in acaDict.items():
    print(k,v)
#get value associated with the key
print(acaDict.get("lName", "Not here")) #not here is if the key does not exist

#delete key value
del acaDict["city"]

for i in acaDict:
    print(i)
#clear or delete all the data inside
acaDict.clear()
#list to hold dictionary

employees = []
fname, lname = input("enter employee name: ").split()
employees.append({'fname': fname, 'lname': lname})

print(employees)
    
'''
'''
#dictionary workout

def addCustomer():
    fname, lname = input('Enter customer name: ').split()
    customers.append({'fname': fname, 'lname': lname})

def checkEntry():
    if enterCustomer != 'y':
        
        if enterCustomer != 'n':
            print('must enter y or n')
    
customers = []


while True:
    enterCustomer = input("Enter customer Y/N: ")
    checkEntry()
    if enterCustomer == 'y':
        addCustomer()
    if enterCustomer == "n":
        for i in customers:
            print(i['fname'].capitalize(), i['lname'].capitalize())
        break
'''

'''
recursive functions

'''     
'''
#factorials 
def factorial(num):
    if num <= 1:
        return 1
    else:
        result = num * factorial(num-1)
        return result
   
print(factorial(5))
'''
#fibonacijev niz
def fibonaci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    
    else:
        return fibonaci(num-1) + fibonaci(num-2)

print(fibonaci(6))
        







