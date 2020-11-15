#? __init__() function

'''
1. It is a built-in function.

2.All classes have a function called __init__(), which is always executed 
 when the class is being initiated or i.e. when object is created .
 
3.Use the __init__() function to assign values to object properties, 
 or other operations that are necessary to do when the object is being created.
 
4.The __init__() function is called automatically every time the class is being used to create 
  a new object.

5. init method is a constructor(which is always executed when the class is being initiated),
  which first argument is an object .
  
  And here our object is "self",which we have to call by default.
  
 6. constructor deside how much memory require your variable in heap memeory.
  
  '''
  
  class person:			#! create a class
  
    def __init__(self,fname,lname,age):  # init built-in constructor and self object
	
        #instance variable : first_name,last_name,age.full_name
        print("constructor init ,method is called")
		
        self.first_name=fname
        self.last_name=lname
        self.age=age
        self.full_name=fname+' '+lname
		
p1=person("sahil","mund",20)
p2=person("sammy","daniel",21)
# p1 and p2 are objects 

print(p1.first_name)
print(p2.last_name)
print(p1.full_name)

----------------------------------------------------------------------------

#?	Normal Class Vs Class with init method



class MyComputer: #! create a class

  def config(self): #! create a blueprint for instance
      print("i5,16gb,1tb")

comp1 = MyComputer() #! create an object
# print(type(comp1))    
MyComputer.config(comp1) #! call object 1
comp1.config() #! call object 2

#? special method __init__

class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
        print("processor",cpu,ram) # no need to call the method init automatically call when we create object
    def config(self):
        print("config is",self.cpu,self.ram)


com = Computer('i5',16) # here we pass 3 arg 1 is the object itself cpu & rams
com.config()

#? CONSTRUCTOR 
#! constructor deside how much memory require your variable in heap memeory
