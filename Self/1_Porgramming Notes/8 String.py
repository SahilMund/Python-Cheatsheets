
# !STRING #
#?Strings are Arrays 
#A string is immutable.

a = "Hello, World!"
print(a[0]) #remember that the first character has the position 0

#?Slicing
print(a[-1])  //lat value will print


b = "Hello, World!" 
print(b[2:5]) #Get the characters from position 2 to position 5 

#[first index : no of items to print]

#? Negative Indexing

b = "Hello, World!"
print(b[-5:-2]) #Get the characters from position 5 to position 1, starting the count from the end of the string

#?String Length

print(len(a))

#? strip()
#The strip() method removes any whitespace from the beginning or the end
print(a.strip())
print(a.lstrip())		# removed only left site spaces
print(a.rstrip())		# removed only right site spaces

#? lower() & upper()
print(a.lower())
print(a.upper())
print(a.capitalize())  	#only the first letter will be capitalised
print(a.swapcase()) 	# changes from lower to upper or upper to lower


#? check the case of the string
Str="hello sahil"
print(Str.islower())
print(Str.isupper())
print(Str.isalpha())

#? replace()
x="Sahil x Mund"
print(x)
print(a.replace('x','R'))
print(a.replace('x','Ranjan'))
print(x)

#? split()
m = "Hello, World!"
print(m.split(",")) # returns ['Hello', ' World!']


# find() method
#To find the position of any value from a string
m="hey my name is sahil , and urs is ?"

print(m.find("is"))

# center() method
# here stars first print in right side then left side
name="sahil"
print(name.center(9,"*"))		#    **sahil**
print(name.center(10,"*"))		#	 **sahil***



#? Check String
#To check if a certain phrase or character is present in a string, we can use the keywords in or not in

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

x = "ain" not in txt
print(x) 

#? String Concartinate

a = "Hello"
b = "World"
c = a + b
print(c)
d = a + " " + b
print(d)

#? String Format

age = 36
tx = "My name is John, I am " 
tx = "My name is John, I am " + age
print(tx) #its not working thats why we use string formating
tx = "My name is John, I am {}"
print(tx.format(age))

#formatting inside print

#1.using %
name='sahil'
age=20
per = 90.5

print("The name is %s  and the age is %d with the percentage of %.2f " %(name,age,per))


#2.using format specifiers -- by default {0} {1}
print("The name is {} and age is {}".format(name,age))

#==print("The name is {0} and age is {1}".format(name,age)) // by default



print("The name is {1} and age is {0}".format(name,age))

#//////////another way of formatting
name='sahil'
print(f' my name is {name}')

#? for loop  in string and usage of end=""

#printing letter by letter

string=input("Enter your name : ")
for i in string:
	print(i)
	
####################################3

string=input("Enter your name : ")
for i in string:
	print(i,end="")