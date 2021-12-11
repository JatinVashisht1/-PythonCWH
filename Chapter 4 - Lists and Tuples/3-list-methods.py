a = [1,2, 5, 3, 6, 7, 8, 56, -1, -5, -10]

# List Methods

a.sort() # it returns None
print(a)
print(a.sort())

a.reverse() # it will also return None
print(a) # reverse method reverses the list

a.append(69) # appends 69 at the end of the list
# returns None
print(a)

a.insert(3, 54)
#this will insert 54 at index 3
# if we give an index greater then the limit of list then it will insert that element at the end of the list
a.insert(500, 13)
print(a)

print(a.pop(2)) # it will delete element at index 2 and return the value of deleted element

a.remove(-1) # removes -1 from list
# it returns None
print(a)
# a.remove(5462) ## This will give errors
a = {'a', "Jatin", 2, 5}
