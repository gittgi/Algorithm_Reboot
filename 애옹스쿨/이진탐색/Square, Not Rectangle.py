import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

s = 1
e = min(max(arr), n)
ans = 0
while s <= e:
    
    mid = (s+e) // 2
    # 범위 조심!!!
    start = 0
    end = mid
    # mid가 길이
    possible = False
    while end <= n:
        for j in range(start, end):
            if arr[j] < mid:
                start = j+1
                end = start + mid
                break
        else:
            possible = True
            break
    
    if possible:
        ans = max(ans, mid)
        s = mid + 1
    else:
        e = mid - 1


print(ans)