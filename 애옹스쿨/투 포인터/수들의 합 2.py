n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr += [0]

s = 0
e = 0
total = arr[s]
cnt = 0

while e < n:
    if total < m:
        e += 1
        total += arr[e]
    elif total > m:
        total -= arr[s]
        s += 1
    else:
        cnt += 1
        total -= arr[s]
        s += 1
        e += 1
        total += arr[e]

print(cnt)