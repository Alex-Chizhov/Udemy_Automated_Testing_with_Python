import functools

def decorator_with_argument(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func():
            if number == 56:
                print('Not running the function')
            else:
                func()
            print('After the decorator')
        return function_that_runs_func
    return my_decorator

@decorator_with_argument(56)
def my_function_too():
    print('Hello')

my_function_too()


#
# With parameters
#


def decorator_with_argument(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args,**kwargs):
            if number == 56:
                print('Not running the function')
            else:
                func(*args,**kwargs)
            print('After the decorator')
        return function_that_runs_func
    return my_decorator

@decorator_with_argument(57)
def my_function_too(x, y):
    print(x + y)

my_function_too(257, 167)