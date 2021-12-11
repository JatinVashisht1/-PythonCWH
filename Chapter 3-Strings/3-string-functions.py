story = "once upon a time there was blah blah blah lol"

# String Functions

print(len(story))  # returns number of characters in the string

# String.endswith(), returns the whether this string ends with string provided or not
print(story.endswith("..."))
print(story.endswith("ll"))
print(story.endswith("l"))

# String.count(), returns the number of occurences of string provided
print(story.count("a"))
print(story.count("ah"))

# String.capitalize(), returns string by capitalizing first character of the string
print(story.capitalize())

# String.find(word), returns the index of first occurence of the word
print(story.find("blah"))
print(story[27])
print(story.find("jatin"))

# String.replace(old word, new word), returns string by replacing old word with new word
print(story.replace("blah", "random"))
