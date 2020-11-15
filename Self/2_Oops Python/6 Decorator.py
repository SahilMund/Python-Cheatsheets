
#?  Decorator 
'''
decorator is used for class variable.

decorator is predefined in python to define class methods i.e. @classmethod.
'''
class Student:
    school = "sjinstitute"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod   
    def getschool(cls):
        return cls.school 

s1 = Student(20,25,30)
s2 = Student(30,35,30)
print(s1.avg())
print(s2.avg())
print(Student.getschool())



# e,g,2

#class methods
class person:
    count_instance=0
    def __init__(self,fname,lname,age):
        #instance variable
        person.count_instance += 1
        print("constructor ,method is called")
        self.first_name=fname
        self.last_name=lname
        self.age=age

    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} of person classes"

    def full_name(self,x):
        return f"{self.first_name} {x} {self.last_name}"
p1=person("sahil","mund",20)
p2=person("sammy","daniel",21)
print(p1.full_name("ranjan"))
print(person.count_instances())

----------------------------------------------------------------------

#? name mangling :
'''
1.In python all the methods are in public by default, there is no private method.

2.COnvention for private method :  __name

3.Dunder or double underscore (__) method or magic method => __init__

'''
---------------------------------------------------------------

#? Usage of decorators :

#1. @property :

'''
If a function is define with @property decorator ,we don't have to call the function as function just call it as an object.'''

#2. getter decorator


@property
def price(self):
	return self.__price
	

#?  setter decorator

@price.setter
def price(self,new_price):
	self.__price = max(new_price,0)