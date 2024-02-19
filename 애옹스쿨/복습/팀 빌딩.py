import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

s = 0
e = n-1
max_val = 0
while s < e:
    abil = min(arr[s], arr[e]) * (e - s - 1)
    if abil > max_val:
        max_val = abil
    
    if arr[s] > arr[e]:
        e -= 1
    else:
        s += 1

print(max_val)