import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

prefix = [0] * n
suffix = [0] * n

prefix[0] = arr[0]
ans = 0
temp = 0
for i in range(1, n):
    if arr[i] < prefix[i-1]:
        prefix[i] = prefix[i-1]
        temp += 1
    else:
        prefix[i] = arr[i]

if temp >= 2:
    ans = 0
elif temp == 1:
    ans = 1
else:
    ans = n

suffix[n-1] = arr[n-1]
for i in range(n-2, -1, -1):
    if arr[i] > prefix[i+1]:
        prefix[i] = prefix[i+1]
        temp += 1
    else:
        prefix[i] = arr[i]

if temp >= 2:
    ans = 0
elif temp == 1:
    ans += 1
else:
    ans = n

print(ans)