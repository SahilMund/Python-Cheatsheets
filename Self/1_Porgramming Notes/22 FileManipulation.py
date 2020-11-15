
# for doing any operation file must be close otherwise u can't perform any operation
# for creating a file and write something in it

file = open("C:\\Users\\USER\\Desktop\\fm.txt",'w')
# or file = open("C:/Users/USER/Desktop/fm.txt",'w')
file.write("hello world ?? How r u guyss")
file.close()

#? to give  the access to pyhton for autoclosing the files

with open("C:\\Users\\USER\\Desktop\\fm.txt",'w') as file:
	file.write("hello world ?? How r u guyss")


#for read the content of a file

file = open("C:\\Users\\USER\\Desktop\\fm.txt",'r')
# or file = open("C:/Users/USER/Desktop/fm.txt",'r+')
print(file.read()) 		
#print(file.read(5))
file.close()

# append to the content of the file

file = open("C:\\Users\\USER\\Desktop\\fm.txt",'a')
# or file = open("C:/Users/USER/Desktop/fm.txt",'a+')
file.write("jjjjjjjjjjjjjjjjjjjj")
file.close()



# for renaming the file
import os
os.rename("C:\\Users\\USER\\Desktop\\fm.txt","C:\\Users\\USER\\Desktop\\renamed.txt")

# for removing the file permanently

import os
os.remove("C:\\Users\\USER\\Desktop\\renamed.txt")

------------------------------------------------------------OS-----------------

import os

#1. making a new directory

os.mkdir("C:\\Users\\USER\\Desktop\\fm")

#2.to get the path of current directory

os.getcwd()

#3.to change the path of current directorydirectory

os.chdir(<path>)

#4.to remove the directory

os.rmdir()

#5. retruns all the name of direcotry in list format

-----------------------------------------------------------------------------

#? tell() method 
#--It  returns the current file location from a file stream

f=open("C:\\Users\\USER\\Desktop\\fm.txt")

print(f'cursor position :  {f.tell()}')
f.close()


#? seek() method 
# to change the current file position in a file stream

f=open("C:\\Users\\USER\\Desktop\\fm.txt")

f.seek(20)
f.close()

#? readLine() method
# it prints only one line from the file but read() prints all line.
print(f.readLine())


print(f.read(10))   	# only 10 lines will print
#? readlines method
# it gives how many line present and content of it.
print(f.readlines)


#? print name of the file
print(f.name)

#? check whether the file is closed or not
print(f.closed)


#? file as a function

with open('file.txt','r') as f:
	data=f.read()
	print(data)
	
#? read file 'file1.txt' and write it's data in 'file2.txt'

with open('file1.txt','r') as rf:
	with open('file2.txt','w') as wf:
		wf.write(rf.read())
	
	

#? How to read a file which contains emoji

with open('emoj.txt','r',encoding-'utf-8') as rf:
	print(f.encoding)
	print(f.read())



----------------------------------------------------------------------



