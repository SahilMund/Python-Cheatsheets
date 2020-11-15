
'''
pass : if we don't want to execute any statement then it is used

break : It breaks the execution of both inner and outer block

continue :  It breaks the execution of only inner block

'''

#pass
age=20
if age>18:
	print("hello")
else:
	pass
	
	
#break

for i in range(1,8):
	if(i==5):
		break
	print(i)
	
	
	
	
#continue

for i in range(1,8):
	if(i==5):
		continue
	print(i)
	
	
	
	
	-----------------------------
	

#global variables

#1. without globale variables

x=5
def func():
	x=7
	return x
	
print(x)
print(func())
print(x)


#2. with globale variables

x=5			#local variable
def func():
	global x
	x=7			#global variable
	return x
	
print(x)
print(func())
print(x)