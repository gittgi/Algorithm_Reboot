arr = [0] * 10001

for i in range(1, 10001):
    number = i
    for j in str(i):
        number += int(j)
    
    if number <= 10000:
        arr[number] = 1

for i in range(1, 10001):
    if arr[i] == 0:
        print(i)