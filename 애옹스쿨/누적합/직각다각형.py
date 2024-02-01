n = int(input())

arrx = [0] * 1000020
arry = [0] * 1000020

x1, y1 = map(int, input().split())
startx, starty = x1, y1
for i in range(n):
    if i == n-1:
        x2, y2 = startx, starty
    else:
        x2, y2 = map(int, input().split())
    if x1 != x2:
        if x2 > x1:
            arrx[x1 + 500000] += 1
            arrx[x2 + 500000] -= 1
        else:
            arrx[x2 + 500000] += 1
            arrx[x1 + 500000] -= 1
    elif y1 != y2:
        if y2 > y1:
            arry[y1 + 500000] += 1
            arry[y2 + 500000] -= 1
        else:
            arry[y2 + 500000] += 1
            arry[y1 + 500000] -= 1


    x1, y1 = x2, y2


max_x = 0
max_y = 0

for i in range(len(arrx)):
    if i == 0:
        continue

    arrx[i] += arrx[i-1]
    arry[i] += arry[i-1]
    if arrx[i] > max_x and i % 2 == 1:
        max_x = arrx[i]
    
    if arry[i] > max_y and i % 2 == 1:
        max_y = arry[i]

print(max(max_x, max_y))