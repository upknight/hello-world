#================================================
# A python code : Recursion 
#------------------------------------------------
# 1. Recursion is a very important concept in
#    functional programming.
# 2. The fundamental part of recursion is
#    self-reference - functions calling
#    themselves. It is used to sovle problem
#    that can be broken up into easier
#    sub-problem of the same type.
#------------------------------------------------
def factorial(x):
    if x==1 :
        return 1
    else:
        return x*factorial(x-1)
#------------------------------------------------
n=int(input("Input a integer number : "))
#------------------------------------------------
print(factorial(n))
#================================================
# vim: ft=python:nu
