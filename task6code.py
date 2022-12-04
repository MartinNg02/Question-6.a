#imports all necessary libraries
import random
from abc import ABCMeta, abstractmethod


class GeneratorStrategy(metaclass=ABCMeta):# Implementing ABC-meta to make our class more robusta and easier to maintain. This also allows us to inherit from other classes.
    @abstractmethod #Setting abstractmethod as default method
    def RandomNumberGenerator(): #every subclasses who wants to use generatorStrategy must have RandomNumberGenerator() 
        '''required'''
        
class MainClass(GeneratorStrategy): #our subclass inheriting GeneratorStrategy pattern.
    def RandomNumberGenerator(): #our generator function
        minRange = int(input("Select min range of the input: ")) #taking in input so set a minium value
        maxRange = int(input("Select max range of the input: "))#taking in input so set a max value
        amount = int(input('Select amount of the input: '))#taking in input so set the lenght of our values
        
        for i in range(amount): #for every index in the lenght given by the input C loop through every index until there is nothing left
            y = random.randint(minRange,maxRange) #for every index in C generate a random number with the given index.
            print (y) #print out the results


    GeneratorTest = RandomNumberGenerator() #Creating a object 
    print(GeneratorTest)
        
  

#The first change 
#The second change
#The third change, hopefully this is correct
