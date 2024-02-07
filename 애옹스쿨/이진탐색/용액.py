import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

min_val = float("inf")
ans = (0, 0)

for i in arr:
    s = 0
    e = n - 1
    while s <= e:
        mid = (s+e) // 2
        target = arr[mid]
        if target != i and abs(target + i) < min_val:
            min_val = abs(target + i)
            ans = (i, target)
        
        if target + i < 0:
            s = mid + 1
        else:
            e = mid - 1

x, y = ans
if x > y:
    x, y = y, x

print(x, y)