t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))

    
    arr.sort(key=lambda x: x[0])
    min_j = arr[0][1]
    cnt = 1

    for i, j in arr[1:]:
        if j < min_j:
 
            cnt += 1
            min_j = j
    
    print(cnt)
