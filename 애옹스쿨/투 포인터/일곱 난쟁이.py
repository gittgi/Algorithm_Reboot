arr = []
for _ in range(9):
    arr.append(int(input()))
total = sum(arr)
target = total - 100

arr.sort()

s = 0
e = 8

while s < e:
    if arr[s] + arr[e] == target:
        for i in range(9):
            if i == e or i == s:
                pass
            else:
                print(arr[i])
        quit()
    
    elif arr[s] + arr[e] > target:
        e -= 1
    else:
        s += 1


