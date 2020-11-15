
#! LIST #
'''
ordered 
changeable / mutable
Allows duplicate members
it can stores integer , string and float value simultaneously
written in []
'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)

thislist[1]="pineapple"

#access the list items by referring to the index
print(thislist[1])
#reverse
print(thislist[-1]) 
#Range 
print(thislist[2:5])
#NOTE: The search will start at index 2 (included) and end at index 5 (not included)
print(thislist[:4]) #print 0 to 4
print(thislist[2:]) #print 2 to end
print(thislist[:])

print(thislist[-4:-1]) # print from -4(include) to -1(not include)

#? CHANGE VALUE
thislist[1] = "blackcurrant"
print(thislist)

#? LIST LENGTH

print(len(thislist))

#? ADD ITEM FROM LIST

#? append
#NOTE The append() method append the specified item
thislist.append("orange")
print(thislist)
print(len(thislist))

#? insert
# NOTE The insert() method insert in specified index
thislist.insert(1, "orange")
print(thislist)

#? REMOVE ITEM FROM LIST

#? remove
# NOTE The remove() method removes the specified item
thislist.remove("orange")
print(thislist)

#? pop 
# NOTE The pop() method removes the specified index, (or the last item if index is not specified)
thislist2 = ["apple", "banana", "cherry"]
thislist2.pop()
print(thislist2)

#? del  -- deleting an item from the list 
#here both memory and items are going to delete
del thislist2[0]
print(thislist2)

#? clear
#NOTE The clear() method empties the list i.e. only the values are deleted not the memory
thislist2.clear()
print(thislist2)

#? COPY ITEM FROM LIST

#? copy
mylist = thislist.copy()
print(mylist)

#? list
mylist2 = list(thislist)
print(mylist2)

#? JOIN LISTS

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#? extend
# NOTE Use the extend() method to add list2 at the end of list1

list1.extend(list2)
print(list1)

#append can change the dimension of original list but extend can't so we have to prefer extend
#e.g:
m=[1,2,3,4]
n=[9,8,7,6]
o=[]
p=[]

o.extend(m)
o.extend(n)
print(o)			#  [1, 2, 3, 4, 9, 8, 7, 6]  --1D

p.append(m)
p.append(n)
print(p)			#	[[1, 2, 3, 4], [9, 8, 7, 6]]  --2D



#max n min  --- in case of integer it choose the max and min value but for characters it choose max and min index number
a=[1,2,3,4,5]
max(a)//5
min(a)//1


#count  -- how many items a item repeated inside the list

a=[1,2,3,4,4,6,7,7,7,9,1,1]
a.count(1)		# 3

#reverse---- for reversing the list according to the index location

a.reverse()
a[-1:]

#sorting

num=[9,6,5,1,0,9,15,24,11]

# ? assending order sorting

num.sort()  #----------mutable         #num.sort(reverse=False)

# ? descending order sorting
num.sort(reverse=True)

num[::-1]

sorted(num)  #--------------immuatble ------------
#Inserting multiple values

list =[]
for i in range(4):
	x=input("enter a number")
	list.append(x)
	
print(list)



#sorting

str="Hi ! Sahil , What's Up ? "
print(sorted(str))


# loops in list
f =['orange','apple','mango']
for fruit in f:
	print(fruit)

