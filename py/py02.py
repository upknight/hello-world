#================================================
# A python code : Generators
# Generators are a type of iterable,
#   like lists or tuples.
# The yield statement is used to define
#   a generator, replacing the return of 
#   a function to provide a result to its
#   caller without destroying local variables.
#------------------------------------------------
def infinite_sevens():
    while True :
        yield 7
#------------------------------------------------
for i in infinite_sevens():
    print(i)
#================================================
# vim: ft=python:nu
