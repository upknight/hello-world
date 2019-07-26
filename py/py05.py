#================================================
# A python code : Decorators 
#------------------------------------------------
# Decorators provide a way to modify functions
#   using other functions. 
#------------------------------------------------
# This is deal when you need to extend the
#   functionality of functions that you don't
#   want to modify.
#------------------------------------------------
# Using generators results in improved
#   performance, which is the result of the
#   lazy (on demand) generation of values,
#   which translates to lower memeory usage.
#   Furthermore, we do not need to wait until
#   all the elements have been generated before
#   we start to use them.
#------------------------------------------------
def decor(func):
    def wrap():
        print("==============")
        func()
        print("==============")
    return wrap
#------------------------------------------------
def print_text():
    print("Hello world!")
#------------------------------------------------
decorated = decor(print_text)
decorated()
#================================================
# vim: ft=python:nu
