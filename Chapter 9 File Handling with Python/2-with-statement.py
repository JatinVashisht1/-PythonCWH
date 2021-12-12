## The best way to open and close file automatically is the "with" statement
with open("test.txt") as f:
    data = f.read() # No need to close file
print(data)
