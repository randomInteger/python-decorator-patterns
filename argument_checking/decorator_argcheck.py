#!/usr/bin/env python3
#decorator_argcheck.py
#Very simple python3 example of using a decorator pattern
#to do reusable input argument checking.
#Author:  Christopher Gleeson, April 2018
from functools import wraps

def check_args_as_str(f):
    """
    A VERY simple decorator that type checks *args
    to ensure ever arg in args is of type str, and
    that there is at least one string argument present.

    Raises:  Generic Exception()
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        if len(args) < 1:
            raise Exception("*args must not be empty!")
        for arg in args:
            if type(arg) is not str:
                print("Error:  Args were:", args)
                raise Exception("*args must contain only strings!")
        print("Calling decorated function")
        return f(*args, **kwargs)
    return wrapper

@check_args_as_str
def example(a,b,c):
    """
    A very boring example function expects to be called
    with three strings and does not check....a good place
    for a reusable decorator.
    """
    print("Called example function with:", " ".join([a,b,c]))

#Begin test section....

#This test should pass
print("Test 1:  example is called with proper args")
example("one","two","three")

#This test should raise an Exception which we will catch to continue
print("\nTest 2: example is called with an arg of the wrong type")
try:
    example("1","2",3)
except Exception as err:
    print("Test 2 caught an Exception:", str(err))
finally:
    print("Continuing on, to Test 3 which should assert on empty args...")


print("\nTest 3: example is called with no args at all...")
example()
