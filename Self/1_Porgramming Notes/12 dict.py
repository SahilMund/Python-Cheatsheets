
#! DICTIONARY #
'''
 unordered
 changeable / MUTABLE
 indexed
 have keys and values  i.e. key value pair
 Each key should be unique(if not then values will be overridden)
 writen in {}
 {KEY : VALUE }
 '''
 
 # features of dictionary:
 1.It is a type of hash table.
 2.it is a unsorted datastructure.
 3.it is a collection of key value pair.
 4.While accessing item(key value pair),python will return the item as tuple.
 5.key can only be string or number but values can be anything.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# Unique keys
#1.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#output:-{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#2.thisdict = {
  "brand": "Ford",
  "brand": "Mustang",
  "year": 1964
}

#output:-{'brand': 'Mustang', 'year': 1964}


#-----------------------------------------------------------
#? Accessing Items /values
x = thisdict["model"]
y = thisdict.get("model")
print(x,y)

#? Accessing Items

thisdict.items()

#? Accessing keys
thisdict.keys()

#? Accessing values
thisdict.values()


#? Changing or updating Values
thisdict["year"] = 2018
print(thisdict)

#? Length
print(len(thisdict))

#? Adding Items
thisdict["color"] = "red"
print(thisdict)

#? Removing Items

thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict) #  removes the last inserted item

del thisdict["model"]
print(thisdict) # you can also delete complete dict

thisdict.clear()
print(thisdict) # empty the dictionary


#? upating
s={"name":"sahil"}
thisdict.update(s)


#? sum,max,min
d={'1':10,'2':20,'3':30}
print(sum(d.values()))
print(max(d.values()))
print(min(d.values()))


# fromkeys() method

d=dict.fromkeys(['name','age','height'],'unknown')
print(d) 			#{'name': 'unknown', 'age': 'unknown', 'height': 'unknown'}

'''
copy also same as list 
'''

