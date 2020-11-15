
#? normal list
list = []
for i in range(20):
	list.append(i)
	

# list cmprehension with for loop
list1=[i for i in range(3)]

list2=[input()  for i in range(3)]


# list comprehension with if stmt
nums=[1,2,3,4]
new_nums=[]
for i in nums:
	if i%2 ==0:
		new_nums.append(i*2)
	else:
		new_nums.append(-i)
		
print(new_nums)


#		=> Using comprehension

nums=[1,2,3,4]
new_nums=[i*2 if i%2==0 else -i for i in nums]

print(new_nums)

--------------------------------------------------------------------------
#dictionary comprehension

sq={f'square of {num} is ' : num **2  for num in range(1,11)}

print(sq)


-------------------------------------
#set cmprehension

s ={k**2 for k in range(1,11)}
print(s)