## FILE HANDLING IN PYTHON

## To create/open file
f = open("test.txt", "w")## Here w is the mode of opening file, w = write mode and r = read mode
f.write("This is sample text")## Writing something to file
f.close() # closing the file

## To read a file, we will open file in read mode
f = open("test.txt", "r")
text1 = f.read() # reading entire content of file
print(text1)
f.close()

f = open("test.txt", "r")
text2 = f.read(2) # reading first two characters of file
print(text2)
f.close()

f = open("test.txt", "w")
f.write("This is appending of line\n")
f.write("This is appending of line")
f.close()

## Different modes for opening a file
# r – open for reading

# w – open for writing

# a – open for appending

# + -> open for updating

# ‘rb’ will open for read in binary mode

# ‘rt’ will open for read in text mode