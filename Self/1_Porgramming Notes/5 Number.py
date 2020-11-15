
# !NUMBER #
"""
 There are thtee types of number 
 int
float
complex
 """

a = 1    # int
b = 2.8  # float
c = 1j   # complex

print(type(a))
print(type(b))
print(type(c))

# !TYPE CASTING #

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
d = float(x)

#convert from float to int:
e = int(y)

#convert from int to complex:
f = complex(x)

print(d)
print(e)
print(f)

print(type(d))
print(type(e))
print(type(f))

# !Random Number #
''' Import the random module, and display a random number between 1 and 9 '''
import random
print(random.randrange(1, 10))		#any number from 1 to 9
print(random.randint(1,10))			#any int value from 1 to 9
print(random.random())				#any point values from 0 to 1

print(random.randrange(1, 100,5))		#stepsize =5 here

print(random.choice([1,4,7]))