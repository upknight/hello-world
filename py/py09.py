#================================================
# A python code : Sets
#------------------------------------------------
#  Sets are data structure, similar to lists
#  or dictionaries. They are created using
#  curly braces, or the set function.
#  They share some functionality with lists,
#  such as the use of in to check whether
#  they contain a particular item. 
#------------------------------------------------
num_set = { 1, 2, 3, 4, 5 }
#------------------------------------------------
word_set = set(["spam","eggs","sausage"])
#------------------------------------------------

#------------------------------------------------
#print(3 in num_set)
#print("spam" not in word_set)
#------------------------------------------------

#------------------------------------------------
#print(num_set)
#print(len(num_set))
#num_set.add(-7)
#num_set.remove(3)
#num_set.remove(2)
#print(num_set)
#print(len(num_set))
#------------------------------------------------

A={1,2,3,4,5}
B={4,5,6,7,8,9}

print("set A = ",A)
print("set B = ",B)
print("set union(A,B), i.e. A | B = ",A|B)
print("set intersection(A,B), i.e. A & B = ",A&B)
print("set difference(A,B), i.e. A - B = ",A-B)
print("set symmetric difference (A,B), i.e. A^B = ",A^B)


#================================================
# vim: ft=python:nu
