'''
Created on Nov 3, 2017

@author: aleksandar.novic
'''
class Animal:
    def __init__(self, birthType = "Unknown", appearance = "Unknown", blooded = "Unknown"):
        self.birthType = birthType
        self.appearance = appearance
        self.blooded = blooded
        
    @property
    def birthType(self):
        return self.__birthType

    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded


    def __str__(self):
        return "A {} is {} it is {} it is".format(type(self).__name__, self.birthType,
                                                  self.appearance, self.blooded)
    
class Mammal(Animal):
    def __init__(self, birthType = "Born alive", appearance = "Fur", blooded = "Warm blooded", nurseYoung = "True"):
        Animal.__init__(self, birthType, appearance, blooded)
        self.nurseYoung = nurseYoung
        
        
        @property
        def nurseYoung(self):
            return self.__nurseYoung
    
        @nurseYoung.setter
        def nurseYoung(self, nurseYoung):
            self.__nurseYoung = nurseYoung

        def __str__(self):
            return super().__str__() + " and it is {} they nurse their young".format(self.nurseYoung)


class Reptile(Animal):
    def __init__(self, birthType = "Born in an egg", appearance = "Dry scales", blooded = "Cold blooded"):
        Animal.__init__(self, birthType, appearance, blooded)
        
    #function overloading, no sense in python
    
    def sumAll(self, *args):
        sum = 0
        for i in args:
            sum+=i
        return sum
    
    
    
def main():
    
    animal1 = Animal("Born alive")
    
    print(animal1.birthType)
    
    
    
    
    
    
main()
    
    
    