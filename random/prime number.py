N = int(input('till what number do you want to check: '))
primenum = []
for num in range(2,N+1):
    count = 0
    for div in range(2,num):
        if num%div == 0:
            count+=1
    if count==0:
        primenum.append(num)
        
print(primenum)




