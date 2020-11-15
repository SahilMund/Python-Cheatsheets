'''
single , multiple , multi level
TODO
super , mro 
'''


#? Inheritance

'''

1.Inheritance allows us to define a class that inherits all the methods and properties 
  from another class.
  
2.Parent class is the class being inherited from, also called base class.

3.Child class is the class that inherits from another class, also called derived class.




'''
class A:
    def feture1(self):
        print("feture 1")
    def feture2(self):
        print("feture 2")

class B(A): #* Means B is inherited from A
    def feture3(self):
        print("feture 3")
    def feture4(self):
        print("feture 4")

a1 = A()
print(a1.feture1())
print(a1.feture2())

a2 = B()
print(a2.feture1())


------------------------------------------------------------

class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
	
'''
When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
'''

'''
To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

Example
'''
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
	

---------------------------------
#? use of super() class
'''
Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

Example'''
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
	
	
	
	'''
By using the super() function, you do not have to use the name of the parent element, 
it will automatically inherit the methods and properties from its parent.'''



-----------------------------------------------------------

#Advantage of using Inheritance :

#?	without using inheritance

class Phone :
	def __init__(self,brand,model_name,price):
		self.brand=brand
		self.model_name=model_name
		self.price=max(price,o)
		
	def full_name():
		return f"{self.brand} {self.model_name}"
		
	def  make_a_call(self,number):
		return f"calling {number}....."
	
class Smartphone :
	def __init__(self,brand,model_name,price,ram,internal_memory):
		self.brand=brand
		self.model_name=model_name
		self.price=max(price,o)
		self.ram=ram
		self.internal_memory=internal_memory
		
	def full_name():
		return f"{self.brand} {self.model_name}"
		
	def  make_a_call(self,number):
		return f"calling {number}....."
		
phone = Phone("nokia","1100",1600)

smartphone=Smartphone("Samsung","G",20000,"6 GB")

print(phone.fullname())

print(smartphone.fullname())



'''
Here DRY(DO nor repeat ur self ) doesnot satisfy so we should go for inheritance '''


#?	by using inheritance


class Phone :				#parents or base class
	def __init__(self,brand,model_name,price):
		self.brand=brand
		self.model_name=model_name
		self.price=max(price,o)
		
	def full_name():
		return f"{self.brand} {self.model_name}"
		
	def  make_a_call(self,number):
		return f"calling {number}....."
	
class Smartphone :
	def __init__(self,brand,model_name,price,ram,internal_memory):
		'''self.brand=brand
		self.model_name=model_name
		self.price=max(price,o)'''
		
		# 2 ways to access parent classs
		
		#1. using class
		Phone.__init__(self,brand,model_name,price)
		
		#2. using super() keyword
		super().__init__(brand,model_name,price)
		
		self.ram=ram
		self.internal_memory=internal_memory
		
	'''	
	def full_name():
		return f"{self.brand} {self.model_name}"
		
	def  make_a_call(self,number):
		return f"calling {number}....."'''
		
phone = Phone("nokia","1100",1600)

smartphone=Smartphone("Samsung","G",20000,"6 GB")

print(phone.fullname())

print(smartphone.fullname())



----------------------------------------------------------------

#? MRO
# Method Resolution Order---
# By default the parent class "Phone" will inherit  this " builtins.object"

print(help(Smartphone))

# output:
 '''
 Smartphone
 Phone
 builtins.object
 '''
---------------------------------------------------------------------------

#? isinstance() 

#  It is used to check whether an object belongs to a class or not and if yes it return True .

isinstance(phone,Phone)


------------------------------------------------------------------------

#?	issubclass()

#it is used to check whether a class is inherit another class or not.

issubclass(Smartphone,Phone)

