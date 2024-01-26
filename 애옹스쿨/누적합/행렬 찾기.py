import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(list(map(int, input().split())) for _ in range(n))

prefix = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + arr[i-1][j-1]

print(prefix)