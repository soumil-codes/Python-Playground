array = list(map(int, input('enter space separated numbers: ').split()))
print(array)

b = array.count(20)
c = array.count(3)
if b==2 and c==3:
    print('yes')
else:
    print('no')