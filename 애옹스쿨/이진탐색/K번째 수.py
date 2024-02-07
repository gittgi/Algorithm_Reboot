n = int(input())
k = int(input())
s = 1
e = n * n
ans = 0
while s <= e:
    mid = (s+e) // 2
    cnt = min(mid, n)
    for i in range(2, n+1):
        cnt += (mid // i)

    
    if cnt >= k:
        ans = mid
        e = mid - 1
    else:
        s = mid + 1
    

print(ans)