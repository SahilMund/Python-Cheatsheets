
#?Polymerphism

'''

1.Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).

2.Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle).
 However we could use the same method to color any shape.This concept is called Polymorphism.
'''

class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)

'''
Output

Parrot can fly
Penguin can't fly
In the above program, we defined two classes Parrot and Penguin. Each of them have a common 
fly() method. However, their functions are different.

To use polymorphism, we created a common interface i.e flying_test() function that takes 
any object and calls the object's fly() method. Thus, when we passed the blu and peggy objects
 in the flying_test() function, it ran effectively.


'''


--------------------------------------------------------------------------------------------------------


'''
multiple  behaviour of an object is called as polymorphisim.

1> Duck Typing
2> Operator Overloading
3> Operator Overriding
4> Method Overriding
'''
#? DUCK TYPING
'''
if it look like a duck,
swims like a duck,
quack like a duck,
then it is probabily is a duck

means dynamic typing
ex : x = 5 type of x is intiger
now  x = "spandan" type of x is string 
'''
class PyCharm:
    def exicute(self):
        print("compiling")
        print("Running")

class myEditor:
    def exicute(self):
        print("compiling")
        print("Running")
        print("spell check")

class laptop:
    def Code(self,ide):
        ide.exicute()

ide = PyCharm() 
# there is an object ide and it has the methhod exicute thatshit .
# we doesn't neet to concern about ide
lap1 = laptop()
lap1.Code(ide)

#? OPERATOR OVERLOADING
'''
same method but type of arguments are different
5+6
5 & 6 = operands & + is operator
methods for operators
+ = __add__()
- = __sub__()
'''

class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)
        return s3

s1 = student(58,30)
s2 = student(50,46)

s3 = s1 + s2
print(s3.m1)

#? METHOD OVERLOADING & METHOD OVER RIDING
'''
#! Over Loading
in one class multiple method with same name is called method overloading
class student :
   def avarage(a,b)
   def avarage(a,b,c)
#! Over riding
multiple method with same name and same parameter is called method over riding
'''
# class students:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
    
#     def sum(self,a=None,b=None,c=None):
#         s = a+b+c
#         return s

# s1 = students(58,30)
# print(s1.sum(5,6))
