d = {
    "name": "XYZ",
    "UID": "ABC",
    "Marks": [55, 32, 49, 54, 45],
    "S No.": 69,
    12 : "Can contain numbers in key also",
    'j': "Can contain characters in key also",
    True: False,
    "dict": {"Jatin": "Vashisht"}
}

## ways to print dictionary elements
# d.get() method will not throw error if we enter wrong key 
# d["key"] way will throw error if we enter wrong key
print(d.get("name"))
print(d["name"])
print(d.get("Wrong key")) # This will not throw an error
# print(d["wrong key"]) ## This will throw an error
print(d["dict"]["Jatin"])

print(d) # To print whose dictionary with key and value

print(d.keys())# Method to print keys only
print(d.values())# Prints values of dictionary

##Properties of Dictionary
# It is unordered
# It is mutable
# It is indexed
# Duplicate keys are not allowed