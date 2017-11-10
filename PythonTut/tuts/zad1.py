'''
Created on Oct 30, 2017

@author: aleksandar.novic
'''

investment, interest = input("Enter investment and interest: ").split()

investment = int(investment)
interest = int(interest) * .01

for i in range(10):
    investment = investment + investment * interest
    
    print("Earnings in year {} is {:.2f}".format(i, investment))


