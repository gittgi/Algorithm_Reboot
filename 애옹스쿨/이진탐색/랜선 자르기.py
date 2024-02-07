k, n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))

s = 1
e = sum(arr)
ans = 0
while s <= e:
    mid = (s+e) // 2
    lans = 0
    for i in arr:
        lans += i // mid
    
    if lans >= n:
        ans = max(ans, mid)
        s = mid + 1
    else:
        e = mid - 1

print(ans)
