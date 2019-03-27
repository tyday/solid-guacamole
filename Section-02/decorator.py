import functools

def my_decorator(func):
    @functools.wraps(func)
    def func_that_runs_func():
        print('in the decorator')
        func()
        print('after the decorator')
    return func_that_runs_func

@my_decorator
def my_function():
    print('im the function!!')

# my_function()

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("in the decorator")
            if number == 56:
                print('Not running the function')
            else:
                func(*args, **kwargs)
            print('after the decorator')
        return function_that_runs_func
    return my_decorator


@decorator_with_arguments(57)
def my_function_too(*args):
    print('Hello', *args)

my_function_too(57,79)