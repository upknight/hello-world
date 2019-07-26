#================================================
# A python code : Generators
#------------------------------------------------
# Generators are a type of iterable,
#   like lists or tuples.
#------------------------------------------------
# The yield statement is used to define
#   a generator, replacing the return of 
#   a function to provide a result to its
#   caller without destroying local variables.
#------------------------------------------------
# Using generators results in improved
#   performance, which is the result of the
#   lazy (on demand) generation of values,
#   which translates to lower memeory usage.
#   Furthermore, we do not need to wait until
#   all the elements have been generated before
#   we start to use them.
#------------------------------------------------
def make_word(x):
    word=""
    for ch in x:
        word+=ch
        yield word 
#------------------------------------------------
#for i in numbers(12):
#    print(numbers(11))
#    print(i)
#------------------------------------------------
print(list(make_word("China")))
#================================================
# vim: ft=python:nu
