n = int(input())
arr = list(map(int, input().split()))

s = 0
e = n - 1

min_val = 2000000000
min_s = 0
min_e = 0


while s < e:
    if abs(arr[s] + arr[e]) == 0:
        print(arr[s], arr[e])
        quit()
    if abs(arr[s] + arr[e]) < min_val:
        min_val = abs(arr[s] + arr[e])
        min_s = s
        min_e = e
 
    
    if arr[s] + arr[e] > 0:
        e -= 1
    else:
        s += 1

print(arr[min_s], arr[min_e])
