#================================================
# A python code : Generators
# Generators are a type of iterable,
#   like lists or tuples.
# The yield statement is used to define
#   a generator, replacing the return of 
#   a function to provide a result to its
#   caller without destroying local variables.
#------------------------------------------------
# Using generators results in improved
#   performance
#------------------------------------------------
def numbers(x):
    for i in range(x) :
        if i%2==0:
            yield i
#------------------------------------------------
#for i in numbers(12):
#    print(numbers(11))
#    print(i)
#------------------------------------------------
print(list(numbers(20)))
#================================================
# vim: ft=python:nu
