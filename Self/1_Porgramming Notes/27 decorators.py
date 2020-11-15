
#? decorators
'''
In Python, functions are the first class objects, which means that –

Functions are objects; they can be referenced to, passed to a variable and returned from other functions as well.
Functions can be defined inside another function and can also be passed as argument to another function.
Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.

In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

It is a function which enhance the functionality of a function. '''





def decorator_func(any_func):
        def wrapper_func():
                print('this is awsm function')

                any_func()

        return wrapper_func

@decorator_func
def f1():
        print('this is function 1')
f1()


@decorator_func
def f2():
        print('this is function 2')
f2()

''' in the above code

@decorator_func means --- 
	fun1=decorator_func(f1())
	fun1()
	
@decorator_func means --- 
	fun2=decorator_func(f2())
	fun2()
	
'''

'''output will be:
this is awsm function
this is function 1
this is awsm function
this is function 2
'''