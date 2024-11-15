# value = 1 
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1
    
names = ["Alanna", "Luke", "Z"]
for x in names:
     print(x)
    
# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x == "Luke":
#         continue
#     print(x)

for x in range(4):
    print(x)

for x in range(2,4):
    print(x)
    
for x in range(5, 101, 5):
    print(x)
else:
    print("Glad that\'s over")

names1 = ["Alanna", "Luker", "Lukel"]
actions = ["valorant", "melee", "elden ring"]

# for name in names1:
#     for action in actions:
#         print(name + " " + action +".")
        
for action in actions:
    for name in names1:
        print(name + " " + action +".")