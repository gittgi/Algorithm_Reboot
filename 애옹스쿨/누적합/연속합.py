import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))

prefix = [0] * (n+1)

for i in range(1, n+1):
    prefix[i] = prefix[i-1] + arr[i-1]

min_prefix = [0] * (n+1)

for i in range(1, n+1):
    min_prefix[i] = min (min_prefix[i-1], prefix[i-1])

ans = -float("inf")

for i in range(1, n+1):
    ans = max(ans, prefix[i] - min_prefix[i])

print(ans)