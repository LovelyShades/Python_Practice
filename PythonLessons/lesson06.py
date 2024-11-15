#Dictionaries and Sets
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)

#acsess items
print(band["vocals"])
print(band.get("guitar"))

#list all keys
print(band.keys())

#list all values
print(band.values())

#print key/value pairs
print(band.items())

#verify a key exists
print("guitar" in band)
print("triangel" in band)

#change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPj"})

print(band)
#remove items
print(band.pop("bass"))

band["drums"] = "Bonham"
print(band)

print(band.popitem())
print(band)

band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# band2 = band #creating a reference
# print("Bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

#correct way to copy
band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy!")
print(band)
print(band2)

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["name"])

#Sets
nums = {1, 2, 3, 4}

nums2 = set((1,2,3,4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

#True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

nums.add(8)
print(nums)

morenums = {5, 6, 7}
nums.update(morenums)
print(nums)
#you can use update with lists, tuples, and dictionaries too

# Merge two sets to create a new set
one = {1, 2 ,3} 
two = {5, 6 ,7}

mynewset = one.union(two) 
print(mynewset)

#keep only dupes
one = {1, 2 ,3} 
two = {2, 3 ,4}

one.intersection_update(two)
print(one)

#keep everything except dupes
one = {1, 2 ,3} 
two = {2, 3 ,4}

one.symmetric_difference_update(two)
print(one)
