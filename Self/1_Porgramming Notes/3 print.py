
# printing and assignment of values


#1. assignments.

a=10
b=30
str="hey my name is sahil"
x=3.0
s='hey'
string="hello 'guys' how are u"
#2.Python supports multiple assignments

a,b,c=50,20,30
a,b,x,str=10,30,3.0,"heyy"
a=b=c=d=e=f=50


#print()

#1. Here  multiplication but addition , division and substraction can;t use in case of strings
print("hyy"*10)

output:hyyhyyhyyhyyhyyhyyhyyhyyhyyhyy

print("abc"+10)   //error

#2.We can print multiple items at a time
a,b,x,str=10,30,3.0,"heyy"
print(a,b,x,str)

#3.\n represents next line

print("hello world")
print("hello \n world")

#4. \t represents tab space
print("hello \t  world")


#5. uses of backslash


\\n  ------  \n
print("hello \\n world")   #output : hello \n world


print("parent\'s group")     #output : parent's group


print("hello "guys" hey")		//error

print("hello \"guys\" hey")		#output : hello "guys" hey



== comparison operator

# is VS ==

#both are used in list comparison

f1 =['orange','apple','mango']
f2 =['orange','apple','mango']

print(f1==f2)		# true -checks values are same or not
print(f1 is f2)		# flase - checks memory are same or not


