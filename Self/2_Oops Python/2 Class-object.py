

#? what is object ?
'''
object is also called as instance
attribute + behaviour = object
attribute ex :- age , name , height (value/variable)
behaviour ex :- wlking , eating (function)
in oop behaviour/function is called method
'''
#? what is class ?
''' blueprint for creating objects 
    in a class we can design an object

    class name :
        arrribute : behaviour
'''





#? class

'''
1.A Class is like an object constructor, or a "blueprint" for creating objects.

2.We can think of class as a sketch of a parrot with labels.
 It contains all the details about the name, colors, size etc. Based on these descriptions, 
 we can study about the parrot. Here, a parrot is an object.
 
3.From class, we construct instances. 

4.An instance(object) is a specific object created from a particular class.

5.The first letter of the class Should be capital .
(not compulsory but we use it capital bcz all the bulit-in class first letter is capital)

6.Inside a class there are more number of function is present which is called as "method".

'''

#?Create a Class

class Parrot:
    pass
	name="It is a bird"
  
  
 '''
 Here, we use the class keyword to define an empty class Parrot. From class,
 we construct instances.An instance is a specific object created from a particular class.'''
--------------------------------------------------------------------------------

#? object

'''
An object (instance) is an instantiation of a class.
 When class is defined, only the description for the object is defined.
 Therefore, no memory or storage is allocated.
 
The example for object of parrot class can be:

obj = Parrot()

Here, obj is an object of class Parrot.

'''

#?Create a object of Class
obj = Parrot()
print(obj.name)




------------------------------------------

#? Modify Object Properties

obj.name="It is a very beautiful bird"


#?Delete Object Properties

del obj.name