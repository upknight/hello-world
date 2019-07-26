#================================================
# A python code : Recursion 
#------------------------------------------------
#  Recursion can also be indirect. One function
#  can call a second, which calls the first,
#  which calls the second, and so on.
#------------------------------------------------
#  This can occur with any number of functions.
#------------------------------------------------
def is_even(x):
    if x==0 :
        return True 
    else:
        return is_odd(x-1)
#------------------------------------------------
def is_odd(x):
    return not is_even(x)
#------------------------------------------------

#------------------------------------------------
n=int(input("Input a integer number : "))
#------------------------------------------------
print(n,"is an even number : ", is_even(n))
#================================================
# vim: ft=python:nu
