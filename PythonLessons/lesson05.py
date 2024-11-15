#arrays

users = ['Dave','John','Sara']

data = ['Dave', 42, True]

emptylist = []

#will tell u if 'Dave' is in the array users
print("Dave" in users)
#prints the spot 0 in array of users
print(users[0])
#prints last spot in array of users
print(users[-1])
#print number in array of value
print(users.index('Sara'))
#print from one point to another in array
print(users[0:2])#excludes Sara
print(users[1:])#includes Sara
print(users[-3:-1])

print(len(data))#prints length

#3 ways to add to lists
users.append('Elsa')
print(users)

users += ['Jason']
print(users)

users.extend(['Robert','Jimmy'])
print(users)

#how to chose position
users.insert(0, 'Bob')
print(users)

#does not replace any starts and stops at placement 2
users[2:2] = ['Eddoe', 'Alex']
print(users)
#starts at 1 and stops at 3. does not include 3
users[1:3] = ['Rockie', 'DP']
print(users)
#removes Bob from list
users.remove('Bob')
print(users)

del users[0]
print(users)

#del data #deletes entire array
data.clear() #clears contents in array
print(data) 

#---------------------------#
#sorting lists
users += ['dave']
users.sort()
print(users)
#note that lowercase is sorted at the end
users.sort(key=str.lower)
print(users)
#use key=str.lower to fix
nums = [4,42,78,1,5]
nums.reverse()
print(nums)

#sort in reverse
nums.sort(reverse=True)
print(nums) 

#3 ways to copy
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
print(mycopy)

