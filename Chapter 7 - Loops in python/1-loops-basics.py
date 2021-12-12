a = 0
while a<100:
    print(a)
    a = a+1

print("----------------------")

# i = 0
for i in range(0, 100):
    print(i)

print("----------------------")

list = [1, 5, 3, 7]
for item in list:
    print(item)

# i = 1
for i in range(10):
    if(i==2):
        continue
    if(i==9):
        break
    print(i)