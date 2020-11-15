
#? map()
'''The map() function executes a specified function for each item in a iterable.
 The item is sent to the function as a parameter.

function :	Required. The function to execute for each item

iterable :	Required. A sequence, collection or an iterator object. You can send as many iterables as you like,
			just make sure the function has one parameter for each iterable.e.g. list,dict,set,tuple
			
			
Syntax :

map(function, iterables)

'''

num=[1,2,3,4]

def square(a):
	return a**2

sq=list(map(square , num))
print(sq)


#using lambda function :
sq=list(map(lambda a:a**2,num))
print(sq)

#using list comprehension

sq=[i**2 for i in num]
print(sq)
-----------------------------------------------------------------------

#? filter()

'''
The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
i.e. filtering of numbers from a list.


Syntax :

filter(function, iterable)

function	A Function to be run for each item in the iterable
iterable	The iterable to be filtered
'''
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)


----------------------------------------------------------------------------

#? zip() 

'''
The zip() function returns a zip object, which is an iterator of
 tuples where the first item in each passed iterator is paired together,
 and then the second item in each passed iterator are paired together etc.

If the passed iterators have different lengths, the iterator with the least
 items decides the length of the new iterator.


or,
when two differnt list contains related values or info then zip() is used .
Syntax
zip(iterator1, iterator2, iterator3 ...)

'''
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)
print(x)				#<zip object at 0x03CA4210>


#use the tuple() or list() function to display a readable version of the result:

print(list(x))				#[('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica')]
print(tuple(x))				#(('John', 'Jenny'), ('Charles', 'Christy'),('Mike', 'Monica'))



------------------------------------------------------------------------------

#? zip() with *args

l=[(1,2),(3,4),(5,6),(7,8)]

l1,l2=list(zip(*l))
print(l1)			#(1, 3, 5, 7)
print(l2)			#(2, 4, 6, 8)

--------------------------------------------------------------------------

#? all  function

'''
The all() function returns True if all items in an iterable are true, otherwise it returns False.

If the iterable object is empty, the all() function also returns True
'''

# list
mylist = [0, 1, 1]
x = all(mylist)

#tuple
mytuple = (0, True, False)
x = all(mytuple)

#set
myset = {0, 1, 0}
x = all(myset)


#dictionary
#When used on a dictionary, the all() function checks if all the keys are true, not the values.

mydict = {0 : "Apple", 1 : "Orange"}
x = all(mydict)

---------------------------------------------------------------

#? any function

'''
The any() function returns True if any item in an iterable are true, otherwise it returns False.

If the iterable object is empty, the any() function will return False.

'''

# list
mylist = [0, 1, 1]
x = any(mylist)

#tuple
mytuple = (0, 1, False)
x = any(mytuple)

#set
myset = {0, 1, 0}
x = any(myset)


# dict
#When used on a dictionary, the any() function checks if any of the keys are true, 
#not the values.

mydict = {0 : "Apple", 1 : "Orange"}
x = any(mydict)

--------------------------------------------------------
#? doc string
'''

This identifies what our function is does.

Docstrings act as documentation for the class, module, and packages.

Docstrings are represented with closing & opening quotes while comments start with a # at the beginning.

'''

def add(a,b):
	'''This is used to takes 2 nos and it returns its sum '''
	return a+b
	
print(add(2,3))
print(add.__doc__)


'''
output:
5
This is used to takes 2 nos and it returns its sum 
'''


print(sum.__doc__)
'''
Return the sum of a 'start' value (default: 0) plus an iterable of numbers

When the iterable is empty, return the start value.
This function is intended specifically for use with numeric values and may
reject non-numeric types.'''


------------------------------------------------------
#? help()

'''It gives info about the given function or modules'''

help(sum)

'''
output:
Help on built-in function sum in module builtins:

sum(iterable, start=0, /)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.
	'''