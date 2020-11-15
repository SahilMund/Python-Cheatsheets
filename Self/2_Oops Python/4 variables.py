
#? VARIABLES IN OOP PYTHON

'''
instance variable
class / static variable 
'''
class car:
    wheels = 4 # Global variable or class variable
	
    def __init__(self): # self is like a pointer
        self.company = "bmw"
        self.milage = 10

c1 = car()
c2 = car()
c1.company = "audi"
print(c1.company,c1.wheels)
print(c2.company,c2.wheels)
