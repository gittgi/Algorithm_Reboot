arr = list(map(int, input().split()))
arr.sort()

for i in range(1, arr[2] * arr[3] * arr[4] + 1):
    cnt = 0
    for j in arr:
        if i % j == 0:
            cnt += 1
    if cnt >= 3:
        print(i)
        quit()