

array = list(map(int, input('enter space separated numbers: ').split()))

newArray = []

for i in array:
    if i not in newArray:
        newArray.append(i)

newArray.sort()

k = int(input('which largest number do you want to find: '))

print(newArray[-k])