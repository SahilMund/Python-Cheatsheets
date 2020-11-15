
#! FUNCTION #

'''
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.'''


#? Creating a Function

#In Python a function is defined using the def keyword:


#1 .function without any parameter

def my_function():			# function declration
  print("Hello from a function")
 
 my_function()			# function calling stmnt
 
  
#2 . function with  parameter

def displayName(name):
  print("hello " + name)

displayName("sahil")


#3. function with parameter and return stmt
def displayName(name):
          return "hyy"+name
displayName("rishu")


#?Calling a Function
#To call a function, use the function name followed by parenthesis:

def my_function():
  print("Hello from a function")

my_function()




#?default parametrs
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

'''
Parameter vs arguments :
A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.'''

#?arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


#? Return Values

def my_function5(x):
  return 5 * x

print(my_function5(3))

#? Pass

def myfunction():
  pass
  
  
 
#?Recursion
'''
  Recursion is a common mathematical and programming concept. 
  It means that a function calls itself. This has the benefit of meaning that you can
  loop through data to reach a result.'''
  
  def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
  
  
  
  
#? clousers 
'''
It is function returning function
'''


def outer_func():
	print('Inside outer function')
	def inner_func():
		print('Inside inner function')
	return inner_func()
	
outer_func()


-----------------------------------------------------------------------

#! LAMBDA #
'''
A lambda function is a small anonymous function
A lambda function can take any number of arguments, but can only have one expression

syntax : -
lambda arguments : expression
'''

x = lambda a : a + 10
print(x(5))


def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2) # argument for n
print(mydoubler(11)) # argument for a


# without lambda function

def even(a):
	return a%2 == 0
print(even(5))


# with lambda function

even = lambda a: a%2==0
print(even(5))

-----------------------------------------------
#? lambda with if....else


# 1.without lambda function

def func(s):
	if len(s)>5:
		return True
	else:
		return False
		
z=func('abcdefgh')
print(z)	
		
# 2.with lambda function

func = lambda s : True if len(s)>5 else False
print(func('abcdefgh'))

--------------------------------------------------

#? enumerate function

'''
It is also called as enumerate function.

it takes a collection (e.g. a tuple) and returns it as an enumerate object. 
it adds a counter as the key of the enumerate object.



'''



#1. without enumerate 

names=['sahil','tony','bella ciao']
pos=0
for name in names:
	print(f'{pos} : {name}')
	pos+=1
	
#2. with enumerate function
names=['sahil','tony','bella ciao']

for pos , name in enumerate(names):
	print((f'{pos} : {name}')
