import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(list(map(int, list(input().rstrip()))) for _ in range(n))

prefix = [[0] * (m+1) for _ in range(n+1)]


for i in range(1, n+1):
    for j in range(1, m+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + arr[i-1][j-1]

ans = 0
for x2 in range(1, n+1):
    for y2 in range(1, m+1):
        if arr[x2-1][y2-1] == 0:
            for x1 in range(1, x2+1):
                for y1 in range(1, y2+1):
                    if arr[x1-1][y1-1] == 0:
                        total = prefix[x2][y2] - prefix[x1-1][y1] - prefix[x1][y1-1] +prefix[x1-1][y1-1]
                        if total == 0:
                            ans = max(ans, (x2- x1 + 1) * (y2-y1 + 1))
print(ans)
print(prefix)