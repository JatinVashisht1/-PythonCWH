
## Set in python

# Syntax
s = {1, 5, 35, 5}
print(type(s))
print(s)
# Empty Set
a = {}  # This is interpretted as empty dictionary
print(type(a))
# to make empty set:
a = set()
print(type(a))
a.add(12) # a.add() method is used to add single element in set
print(a)
a.add(12)
print(a)  # It will print only 12 because set does not contain duplicate elements

# a.add([3, 8, 10]) ## We cannot add list to a set because list is mutable
a.add((4,5,6)) # We can add tuple to a set because tuple is immutabl
print(a)
# a.add({"name":"Jatin"}) ## We cannot add dictionary to set like list because dictionary is mutable    

## Properties of set
# Sets are unordered
# Sets are un-indexed
# There is no way to change items in set
# Sets cannot have duplicate values