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
def decor(func):
    def wrap():
        print("==============")
        func()
        print("==============")
    return wrap
#------------------------------------------------
@decor
def print_text():
    print("Hello world!")
#------------------------------------------------
print_text()
#================================================
# vim: ft=python:nu
