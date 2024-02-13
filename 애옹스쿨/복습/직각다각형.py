arr_x = [0] * 1000020
arr_y = [0] * 1000020
x_set = set()
y_set = set()
n = int(input())

x1, y1 = map(int, input().split())
init_x, init_y = x1, y1
x_set.add(x1)
y_set.add(y1)
for i in range(n-1):
    x2, y2 = map(int, input().split())
    x_set.add(x2)
    y_set.add(y2)

    if x1 != x2:
        if x1 > x2:
            arr_x[x2 + 500010] += 1
            arr_x[x1 + 500010] -= 1
        else:
            arr_x[x1 + 500010] += 1
            arr_x[x2 + 500010] -= 1
    
    elif y1 != y2:
        if y1 > y2:
            arr_y[y2 + 500010] += 1
            arr_y[y1 + 500010] -= 1
        else:
            arr_y[y1 + 500010] += 1
            arr_y[y2 + 500010] -= 1
    x1, y1 = x2, y2

x2, y2 = init_x, init_y
if x1 != x2:
    if x1 > x2:
        arr_x[x2 + 500010] += 1
        arr_x[x1 + 500010] -= 1
    else:
        arr_x[x1 + 500010] += 1
        arr_x[x2 + 500010] -= 1

elif y1 != y2:
    if y1 > y2:
        arr_y[y2 + 500010] += 1
        arr_y[y1 + 500010] -= 1
    else:
        arr_y[y1 + 500010] += 1
        arr_y[y2 + 500010] -= 1



prefix_x = [0] * 1000021
prefix_y = [0] * 1000021

for i in range(1, 1000021):
    prefix_x[i] = prefix_x[i-1] + arr_x[i-1]
    prefix_y[i] = prefix_y[i-1] + arr_y[i-1]

max_val = 0

for i in range(1000021):
    if i not in x_set and prefix_x[i] > max_val:
        max_val = prefix_x[i]
    
    if i not in y_set and prefix_y[i] > max_val:
        max_val = prefix_y[i]

print(max_val)