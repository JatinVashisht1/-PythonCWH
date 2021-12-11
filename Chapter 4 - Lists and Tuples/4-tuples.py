## Tuple is an immutable list

t = (3, 5, 2, 6, 20) # Syntax
print(t[0])
# t[0] = 89 ## This will give an error

t = () # Empty tuple

t = (3,) # tuple with one element requires comma at the end otherwise it gives error
print(t[0])