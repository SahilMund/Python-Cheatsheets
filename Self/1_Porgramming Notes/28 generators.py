

#?Generators

'''
1. Generators are iterators.
2.First python converts iterable to iterators by self calling iter() function,then we can use
 our required operations.
 
3.Generators are iteraors which is a sequence but list is also a sequence but it is iterable.

4.yield is a keyowrd not a function.


'''


#? Itearble(list,dict,set,tuple) Vs iterator

'''
Iterable is an object, which one can iterate over. It generates an Iterator when passed to 
iter() method. Iterator is an object, which is used to iterate over an iterable object using
__next__() method. Iterators have __next__() method, which returns the next item of the object.

Note that every iterator is also an iterable, but not every iterable is an iterator.
For example, a list is iterable but a list is not an iterator. An iterator can be created 
from an iterable by using the function iter(). To make this possible, the class of an object 
needs either a method __iter__, which returns an iterator, or a __getitem__ method with 
sequential indexes starting with 0.
'''

iterable = [1,2,3,'sahil']		  #iterable
iterator = iter(iterable) 		  # iterator

print(iterable)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

'''
output:
[1, 2, 3,'sahil']
1
2
3
sahil



in the above program a sequence is generated but not all the 4 values present in the memory
only one value is allocated when we call next then it allocates next value for which less memory
required and incresase the performance in the list.
'''

#? yield

'''
The yield statement suspends function’s execution and sends a value back to the caller,
but retains enough state to enable function to resume where it is left off. When resumed, 
the function continues execution immediately after the last yield run. This allows its code 
to produce a series of values over time, rather than computing them at once and sending them 
back like a list. '''


---example-----------
# A generator function that yields 1 for first time, 
# 2 second time and 3 third time 
def simpleGeneratorFun(): 
    yield 1            
    yield 2            
    yield 3            
   
# Driver code to check above generator function 
for value in simpleGeneratorFun():  
    print(value) 

'''
Output :

1
2
3
'''



#There are two terms involved when we discuss generators.
#? 1.Generator-Function :
'''
A generator-function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. 
If the body of a def contains yield, the function automatically becomes a generator function.'''


'''example'''

# A generator function that yields 1 for first time, 
# 2 second time and 3 third time 
def simpleGeneratorFun(): 
    yield 1            
    yield 2            
    yield 3            
   
# Driver code to check above generator function 
for value in simpleGeneratorFun():  
    print(value) 

'''
Output :

1
2
3
'''


#2.Generator-Object : 
'''Generator functions return a generator object. Generator objects are used either
 by calling the next method on the generator object or using the generator object in a “for in”
 loop (as shown in the above program).'''
 
 
 ------example-----------
 
# A Python program to demonstrate use of  
# generator object with next()  
  
# A generator function 
def simpleGeneratorFun(): 
    yield 1
    yield 2
    yield 3
   
# x is a generator object 
x = simpleGeneratorFun() 
  
# Iterating over the generator object using next 
print(x.next()) # In Python 3, __next__() 
print(x.next()) 
print(x.next()) 

'''
Output :
1
2
3'''

#So a generator function returns an generator object that is iterable, 
#i.e., can be used as an Iterators .

