def hello_world(): 
    print("Hello World")

hello_world()

value = True

while value:
    print(value)
    value = False

value = True
count = 0

while value:
    count += 1
    print(count)
    if (count ==5):
        break
    else:
        continue

