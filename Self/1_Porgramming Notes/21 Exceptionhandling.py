

# Exception means run time error
# it helps to handle the errors


'''try block and except block are complement to each other , i.e. only one block can run'''
#? try.....except block

x= int(input("enter 1st number : "))
y= int(input("enter 2nd number : "))

try:
	z=x/y
	print(z)
except:
	print("You can't divide a number by zero")
	
	


#? try ....except...else

x= int(input("enter 1st number : "))
y= int(input("enter 2nd number : "))

try:
	z=x/y

except:
	print("You can't divide a number by zero")
	

else:
	print(z)
	


#? try ....except...else.....finally
'''
When try block executed then only else block executed but if instead of try block except block
will execute then else block will be skipped , but finally block will always wxecuted.'''

x= int(input("enter 1st number : "))
y= int(input("enter 2nd number : "))

try:
	z=x/y

except:
	print("You can't divide a number by zero")
	

else:
	print(z)
	
finally:
	print("Succesfully completed exception handling....")
	
--------------------------------------------------------------------------

#? built-in errors
'''
Synatx error , identation error , name error, index error , value error ,key error,
type error , attribute error '''

#? raise built-in errors

def add(a,b):
	if(type(a) is int) and (type(b) is int):
		return a+b
	
	raise TypeError("OOPS !! U r passing wrong data format .")
	
print(add('2','3'))



# Userdefined / custom exception
# It is just use to increase the redability of programmers

class NameTooShortError(ValueError):
    pass

def validate(name):
    if len(name)<6 :
        raise  NameTooShortError('Name is too short  , plz kindly change ur username')

username=input("Enter Your Username :")
validate(username)
print(f' Hello  {username} ')
        



