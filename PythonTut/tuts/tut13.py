'''
Created on Nov 10, 2017

@author: aleksandar.novic
'''

# sampStr = iter("sample")
# 
# print("char: ", next(sampStr))
# print('char: ', next(sampStr))
'''
class Alphabet:
    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index = -1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.letters)-1:
            raise StopIteration
        
        self.index +=1
        return self.letters[self.index]

alpha = Alphabet()

for letter in alpha:
    print(letter)
'''

# person = {'fname' : 'Derek','lname' : 'Banas'}
# 
# for key in person:
#     print(key, person[key])

'''
class Fibonacci:
    def __init__(self):
        self.first = 0
        self.second = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        fibSum = self.first + self.second
        self.first, self.second = self.second, fibSum
        return fibSum
    
fibby = Fibonacci()
    
for i in range(11):
    print("Fib {}: {}".format(i+1, next(fibby)))
'''    
    
'''
LIST COMPREHENSIONS   
'''
# map
print(list(map((lambda x: x*2), range(1,11))))    
# list comprehension
print([2* x for x in range(1,11)])
# filter
print(list(filter((lambda x: x%2 != 0), range(1,11))))
# list comprehension, formulae must be on the right side unlike filter and map
print([x for x in range(1,11) if x%2 !=0])
# list comprehension that acts like map and filter on one line    
#generate 50 values, take to the power of 2, return multiples of 8
print([i ** 2 for i in range(50) if i %8 ==0])

#multiply all values of one list with all values of other list

print([x * y for x in range(1,5) for y in range(4, 20)])    
    
#list comprehensions INSIDE OF LIST COMPREHENSIONS
#generate a list of 10 values, multiply them by 2, return multiples of 8
print([x for x in [i*2 for i in range(10)] if x % 8 == 0])

#PROBLEM
#generate a list of 50 random values between 1 and 1000 and return those that are
#multiples of 9

import random
# print([i for i in [x for x in random.randrange(50)] in range(1000) if x % 9 == 0])
print([x for x in[random.randint(1, 1001) for i in range(50)] if x % 9 == 0]) 
 
#work with mutidimensional list with list comprehension
multiList = [[1,2,3],
             [4,5,6],
             [7,8,9]]
#print 2 5 8
print([col[1] for col in multiList])
#diagonal
print([multiList[i][i] for i in range(len(multiList))])
'''
   works like this, first gives 0,0 position, then 1,1 and at the end 2,2
''' 
    
#GENERATOR FUNCTIONS
#generates individual values one at the time, it creates result overtime instead of all at once

def isprime(num):
    for i in range(2, num):
        if (num%i)==0:
            return False
    return True
    
def gen_primes(max_number):
    for num1 in range(2, max_number):
        
        if isprime(num1):
            yield num1

prime = gen_primes(50)
print('Prime: ', next(prime))
print('Prime: ', next(prime))
print('Prime: ', next(prime))
print('Prime: ', next(prime))
print('Prime: ', next(prime))
print('Prime: ', next(prime))


#GENERATOR EXPRESSIONS 
#looks like list comprehensions but returns results one at the time
#surrounded by ( ) instead of [ ] like LC

double = (x * 2 for x in range(1,10))
print('Double: ', next(double))
print('Double: ', next(double))

for num in double:
    print(num)
