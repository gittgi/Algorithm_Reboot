n = int(input())
arr = list(map(int, input().split()))


# e - s - 1 * min(arr[e], arr[s])

s = 0
e = n - 1
ans = 0

while s < e:

    teamwork = (e - s - 1) * min(arr[e], arr[s])
    ans = max(ans, teamwork)

    if arr[s] > arr[e]:
        e -= 1
    else:
        s += 1

    

print(ans)

