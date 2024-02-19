N, M = map(int, input().split())

arr = list(map(int, input().split()))

s = 0
e = 0
cnt = 0
total = arr[0]

while s < N:
    if total == M:
        cnt += 1
        s += 1
        e = s
        total = arr[s]
    else:
        if total > M:
            
