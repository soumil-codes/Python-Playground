# # Lists to represent keys and values
# keys = ['a','b','c','d','e']
# values = [1,2,3,4,5]

# # but this line shows dict comprehension here
# myDict = { k:v for (k,v) in zip(keys, values)}

# zip(keys, values)
# print(keys)
# print(values)
# We can use below too
# myDict = dict(zip(keys, values))

print ([1,2,3] == [1,3,2])

dic = {1: 3}

dic2 = {2: 5, 4: 6}

dic.update(dic2)
print(dic)
