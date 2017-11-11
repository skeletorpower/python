'''
Created on Nov 11, 2017

@author: aleksandar.novic
'''
#THREADS

import threading
import time
import random

'''
def executeThread(i):
    print("Thread sleeps at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))

    randSleepTime = random.randint(1,5)
    
    time.sleep(randSleepTime)
    
    print("Thread {} stops sleeping at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))


for i in range(10):
    thread = threading.Thread(target=executeThread, args=(i,))
    thread.start()


    print("Active Threads : ", threading.activeCount())
    print("Thread objects :", threading.enumerate())
'''

#SUBCLASSING A THREAD OBJ AND DEFINE WHAT HAPPENS EACH TIME ITS EXECUTED
#INSIDE OF METHOD CALLED RUN
'''
class CustThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    
    def run(self):
        getTime(self.name)

        print("Thread", self.name, "Execution ends")

def getTime(name):
    print("Thread {} sleeps at {}".format(name, time.strftime("%H:%M:%S", time.gmtime())))

    randSleepTime = random.randint(1,5)
    time.sleep(randSleepTime)
    
thread1 = CustThread("1")
thread2 = CustThread("2")

thread1.start()
thread2.start()

print("Thread 1 Alive: ", thread1.is_alive())
print("Thread 2 Alive: ", thread2.is_alive())
print("Thread 1 Name: ", thread1.getName())
print("Thread 2 Name: ", thread2.getName())

thread1.join()
thread2.join()

print("Execution ends")
'''
    
#MOCK MODELING A BANK ACCOUNT WITH THREADS    

class BankAccount(threading.Thread):
    
    acctBalance = 100
    
    def __init__(self, name, moneyRequest):
        threading.Thread.__init__(self)
        self.name = name
        self.moneyRequest = moneyRequest
    
    def run(self):
        threadLock.acquire()
        
        BankAccount.getMoney(self)
        threadLock.release()
        
        
    @staticmethod
    def getMoney(customer):    
        print('{} tries to withdraw ${} at {}'.format(customer.name, customer.moneyRequest, time.strftime("%H:%M:%S", time.gmtime())))

        if BankAccount.acctBalance - customer.moneyRequest > 0:
            BankAccount.acctBalance -= customer.moneyRequest
            print("New account balance : ${}".format(BankAccount.acctBalance))
            
        else:
            print("Not enough money in account")
            print("Current balance: ${}".format(BankAccount.acctBalance))
            
        time.sleep(3)

            
threadLock = threading.Lock()
    
sam = BankAccount("Sam", 20)
billy = BankAccount("Billy", 100)
sally = BankAccount("Sally", 50)
    
sam.start()
billy.start()
sally.start()
    
sam.join()
billy.join()
sally.join()
   
print("Execution ends")
    
    
    
    
    
    
    
    
    


