import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

s = 0
e = max(arr)
ans = 0
while s<=e:
    mid = (s+e) // 2
    temp = 0
    for tree in arr:
        branch = tree - mid
        if branch >= 0:
            temp += branch
    
    if temp >= m:
        ans = max(ans, mid)
        s = mid + 1
    else:
        e = mid - 1

print(ans)