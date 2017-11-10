'''
Created on Oct 20, 2017

@author: aleksandar.novic
'''

# def mult_divide(num1, num2):
#     return (num1 * num2), (num1 / num2)
# 
# mult, divide = mult_divide(5, 4)
# 
# print(mult)
# print(divide)

#return a list 

# def isPrime(num):
#     for i in range(2, num):
#         if(num%i) == 0:
#             return False
#         
#     return True
# 
# def getPrimeList(maxNumber):
#     listOfPrimes = []
#     for num1 in range(2, maxNumber):
#         if isPrime(num1):
#             listOfPrimes.append(num1)
#   
#     return listOfPrimes
# 
# maxNumberToCheck = int(input("Search for primes up to: "))
# 
# listOfPrimes = getPrimeList(maxNumberToCheck)
# 
# for prime in listOfPrimes:
#     print(prime)

#unknown number of arguments

# def sumAll(*args):
#     sum = 0
#     
#     for i in args:
#         sum += i
#     return sum
# 
# print(sumAll(1,2,3,4,5,6,7,8))


import math

def getArea(shape):
    shape = shape.lower()
    if shape == "rectangle":
        rectangleArea()
    elif shape == "circle":
        circleArea()
    else:
        print("Enter rectangle or circle")
        
        
def rectangleArea():
    length = float(input("Enter the length "))
    width = float(input("Enter the width "))
    
    area = length*width
    print("Area of rectangle is ", area)

def circleArea():
    radius = float(input("Enter the radius "))
    area = math.pi * (math.pow(radius, 2))
    
    print("The are of the circle is {:.2f}".format(area))


def main():
    shapeType = input("Get area for what shape: ")
    getArea(shapeType)
    
main()

