n = int(input())

arr = list(map(int, input().split()))

target = int(input())

arr.sort()

s = 0
e = n-1
cnt = 0
while s < e:
    if arr[s] + arr[e] == target:
        cnt += 1
        s += 1
        e -= 1
    else:
        if arr[s] + arr[e] > target:
            e -= 1
        else:
            s += 1

print(cnt)

