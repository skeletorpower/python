'''
Created on Nov 8, 2017

@author: aleksandar.novic
'''

'''
class Sum:
    
    @staticmethod
    def getSum(*args):
        sum= 0
        for i in args:
            sum += i
        return sum
    
    
def main():
    print("Sum is: ", Sum.getSum(1,2,3,4,5))


main()



class Dog:
    num_of_dogs = 0
    
    def __init__(self, name = "Unknown"):
        self.name = name
        
        Dog.num_of_dogs +=1
        
    @staticmethod
    def getNumOfDogs():
        print("There is {} dogs".format(Dog.num_of_dogs))
        
def main():        

    spot = Dog("Spot")
    
    dzeki = Dog("Dzeki")    
        
    spot.getNumOfDogs()    
        
main()
'''  
'''   
class DogNameError(Exception):
    
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

try:
    dogName = input("Enter a dog name: ")
    
    if any(char.isdigit() for char in dogName):
        raise DogNameError
except DogNameError:
    print("Your dogs name can't contain a number")
'''

'''   
num1, num2 = input("Enter 2 values to divide: ").split()

try:
    quotient = int(num1) / int(num2)
    print("{} / {} = {}".format(num1, num2, quotient))   
except ZeroDivisionError:   
    print("U cant divide by zero")
else:
    print("U didn't rais an exception")

finally:
    print("I execute no matter what")   
'''   

try:
    myFile = open(input("Enter file name: "), encoding = "utf-8") 
except FileNotFoundError as ex:
    print("File not found")   
    print(ex.args)
else:
    print(myFile.read())
    myFile.close()
finally:
    print("File successfully opened")
   



        
        
        
        
        
        
        
        
        
        
        
        
        
        
