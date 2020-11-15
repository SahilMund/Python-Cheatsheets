

#? *args (arguements)			*operator e.g:- *a,*b,*c etc

'''NOTE If you do not know how many arguments that will be passed into your function,
 add a * before the parameter name in the function definition.
 
 It is also known as arbitary arguments.
 
 It return a tuple'''

def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Email", "facebook", "wechat")



#? Keyword Arguments
# arg with key = value

def my_function2(child3, child2, child1):
  print("The youngest child is " + child3)
my_function2(child1 = "facebook", child2 = "whatsapp", child3 = "wechat")


\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# e.g 2
def tot(*args):
	print(args)

tot(1,2,3,4,5)


# e.g. -3

def tot(*args):
	print(args)
val=[1,2,3,4,5]
tot(*val)


------------------------------------------------------------
#? *args with normal parameter

def mul(a,b,*args):
	m=1
	print(a,b)						# 1 2
	print(args)						#(3, 4, 5)
	for i in args:
		m*=1
	return m

print(mul(1,2,3,4,5))					# 1

-----------------------------------------------------------------

#? **kwargs (keyword)
'''
It is also called as double star operator or Arbitrary Keyword Arguments.

it gives the output as dictonary.

If the number of keyword arguments is unknown, add a double ** before the parameter name.

'''

--
def my_function3(**kid):
  print("His last name is " + kid["lname"])

my_function3(fname = "Sahil", lname = "Mund")

--------------------------------------------------------------

# precedence to assign parametrs :

def func(name,*args,fname="sahil",**kwargs):
	print(name,args,fname,kwargs)
	
func("Sahil Ranjan Mund",[1,2,3,4,5])


'''
precedence order : - (normal parameter, *args, default parameter , kwargs parameter)

if this order is altered then error will come
'''