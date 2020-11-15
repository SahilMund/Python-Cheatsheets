import math

# squareroot

#1.normally : 
print(4**(1/2))

#2. using sqrt function which is present in math package.
print(math.sqrt(4))


#3. rounding off

print(round(2**0.5,4))


#4.The min() and max() functions can be used to find the lowest or highest value in an iterable:

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#5.The abs() function returns the absolute (positive) value of the specified number:


x = abs(-7.25)

print(x)

#6. The pow(x, y) function returns the value of x to the power of y (xy).


#Return the value of 4 to the power of 3 (same as 4 * 4 * 4):

x = pow(4, 3)

print(x)
-------------------------------------------------------
'''
The Math Module
Python has also a built-in module called math, which extends the list of mathematical functions.

To use it, you must import the math module:

import math
When you have imported the math module,you can start using methods and constants of the module.

'''
import math

x = math.ceil(1.4)
y = math.floor(1.4)
z=math.pi

print(z)

print(x) # returns 2
print(y) # returns 1



-------------------------------------------------

# !Random Number #
''' Import the random module, and display a random number between 1 and 9 '''
import random
print(random.randrange(1, 10))		#any number from 1 to 9
print(random.randint(1,10))			#any int value from 1 to 9
print(random.random())				#any point values from 0 to 1

print(random.randrange(1, 100,5))		#stepsize =5 here

print(random.choice([1,4,7]))