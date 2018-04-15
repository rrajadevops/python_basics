import functools

def my_decorators(func):
    @functools.wraps(func)
    def funtion_that_runs_finc():
        print ("I am in decorator")
        func()
        print ("After decorator")
    return funtion_that_runs_finc

@my_decorators
def my_function():
    print ("In the function")

#my_function()

# decorator with arguments:

def decorator_with_arguments(number):
    def my_decorators(func):
        @functools.wraps(func)
        def funtion_that_runs_finc(*args, **kwargs):
            print ("I am in decorator")
            if number == 75:
                print ("Not running the function")
            else:
                func(*args, **kwargs)
            print ("After decorator")
        return funtion_that_runs_finc
    return my_decorators

@decorator_with_arguments(76)
def my_function_too(x, y):
    print (x + y)

my_function_too(15, 5)