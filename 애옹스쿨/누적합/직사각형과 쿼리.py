import sys
input = sys.stdin.readline


n = int(input())

arr = list(list(map(int, input().split())) for _ in range(n))

prefix = [[[0] * 10 for _ in range(n+1)] for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(10):
            prefix[i][j][k] = prefix[i-1][j][k] + prefix[i][j-1][k] - prefix[i-1][j-1][k]
            if arr[i-1][j-1] - 1 == k:
                prefix[i][j][k] += 1




# print(prefix)


q = int(input())

for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    cnt = 0
    for k in range(10):
        if prefix[x2][y2][k] - prefix[x2][y1-1][k] - prefix[x1-1][y2][k] + prefix[x1-1][y1-1][k] > 0:
            cnt += 1
    
    print(cnt)


