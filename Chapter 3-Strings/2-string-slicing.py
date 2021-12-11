name = "Jatin"
greeting = "Good morning, "
print(greeting + name) # + operator help us concatinating two string literals
c = greeting + name
print(c)
print(name[0])
print(name)
# name[0] = "N" --> does not work

#below statements are example of string slicing
print(name[0:3])
print(name[1:3])
print(name[:3]) # if we leave initial index as blank then it will by default take minimum index of string
print(name[2:]) # if we leave final index as blank then it will by default take maximum index of string
print(name[:]) # this is same as name[0:5], it will take minimum index as initial index and maximum index as final index
# -ve indices can also be used to access elements from back
print(name[-1])
print(name[-2])
print(name[-4:-1]) # now this should be intuitive, this is same as name[1:4]
print(name[1:4])
name = "JatinVashisht"
print(name[0::2])
print(name[0::3])