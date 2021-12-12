
## SET METHODS

s = {5, 6, 3, 7, 12, 90}
print(s)
# s.add(45) adds 45 to set s
s.add(45)
print(s)

# len(s), returns number of elements in set s
print(len(s))

# s.remove(5), removes 5 from set s
s.remove(5)
print(s)
# s.remove(404); ## Throws error because 404 is not present in the set s

# s.pop(), removes random element from set and returns that element
print(s.pop())
print(s)

# s.union({44, 78}), returns a new set with all elements from both sets
print(s.union({44, 78}))

# s.intersection(), returns new set with intersection of both sets
print(s.intersection({6, 7, 78, 404}))