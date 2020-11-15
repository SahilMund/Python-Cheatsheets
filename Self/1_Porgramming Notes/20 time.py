import time

# for creating a time frame
time.time()

# current time and date
time.asctime()

#details about today
time.localtime()

#to delays for 3 seconds
time.sleep(3)
print("Sahil")

#a real life example
# to know in which time or date an user is loggedin , mesage or logged out

import time
# creating time frame for log in , log out and message
log_in=time.time()
msg=time.time()
log_out=time.time()

'''we can't directly convert timeframe to asc time so we have to
 convert it into localtime then convert it into asctime.'''

lin=time.localtime(log_in)
messg=time.localtime(msg)
lout=time.localtime(log_out)

LogIn=time.asctime(lin)
message=time.asctime(messg)
LogOut=time.asctime(lout)

print(LogIn)
print(message)
print(LogOut)
