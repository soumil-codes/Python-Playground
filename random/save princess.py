def find_my_char(lst,char):
    for sublist in lst:
        if char in sublist:
            return list((lst.index(sublist), sublist.index(char)))

def displayPathtoPrincess(n,grid):
    cod_m = find_my_char(grid, 'm')
    cod_p = find_my_char(grid, 'p')
    xm = cod_m[0]
    ym = cod_m[1]
    xp = cod_p[0]
    yp = cod_p[1]

    if xm != xp:
        if xm<xp:
            print("RIGHT \n"*(xp-xm))
        elif xm>xp:
            print("LEFT \n"*(xm-xp))
    if ym != yp:
        if ym<yp:
            print("DOWN \n"*(yp-ym))
        elif ym>yp:
            print("UP \n"*(ym-yp))

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(list(input().strip()))
# print(grid)

displayPathtoPrincess(m,grid)
# a = find_my_char(grid, "m")
# print(a)