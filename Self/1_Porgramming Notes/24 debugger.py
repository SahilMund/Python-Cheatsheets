# debugging

''' It is a process of finding and resolving defects a
 problems wirhin a computer program that prevent the operation '''
 

# why debugging ?

'''
1. our program is not running and causing unexpected errors.
2. our program is working fine but not working the same way we want.

'''

#steps for debugging
'''
1.set trace
2.execute code line by line.
'''

#pdb - python debugger (used for lengthy program to findout the errors)
import pdb
pdb.set_trace()

name=input("Enter ur name :") 
age=input("Enter ur age :") 

print(f'hello {name} and your age is {age}')
age2=int(age)+5

print(f'hello {name} and your age is {age2} in next five years')



# c - ---for exiting the debugger
# n ------- for executing next line