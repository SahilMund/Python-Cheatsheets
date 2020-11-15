
#! TUPLE #
'''
ordered 
unchangeable / IMMUTABLE : this item cannot be  updated but we can add items
written in ()
'''
thistuple = ("apple", "banana", "cherry")


thistuple[3] = "orange" # This will raise an error becouse tuple is unchangeable
print(thistuple)
'''
You cannot remove items in a tuple
But you can delete
'''
#del helps to delete entire tuple

del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#? Create Tuple
thistuple2 = ("apple",)
print(type(thistuple2))   # //Output : <class 'tuple'>

#NOT a tuple
thistuple2 = ("apple")
print(type(thistuple2))   	#//output: <class 'str'>


#indexing

print(thistuple[2])
'''
Accessing , Indexing , Range , Length & Join  same as List 
'''