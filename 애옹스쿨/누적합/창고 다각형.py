n = int(input())
arr = [0] * 1001
for _ in range(n):
    i, h = map(int, input().split())
    arr[i] = h

prefix = [0] * 1002
suffix = [0] * 1002


for i in range(1, 1002):
    prefix[i] = max(prefix[i-1], arr[i-1])

for i in range(1000, -1, -1):
    suffix[i] = max(suffix[i+1], arr[i])

ans = 0
for i in range(1, 1002):
    ans += min(prefix[i], suffix[i-1])

print(ans)
