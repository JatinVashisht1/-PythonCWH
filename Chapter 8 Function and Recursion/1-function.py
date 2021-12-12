def func1(): ## Syntax
    print("Hello")

func1() # Function call

def func12(name): # Function with parameter
    print("Hello", name)

func12("Jatin")

def func13(name):
    greet = "Hello " + name
    return greet # Function with return type

print(func13("Jatin"))

def func14(name = "Jatin"): # Function with return type
    print("Hello", name)

func14()