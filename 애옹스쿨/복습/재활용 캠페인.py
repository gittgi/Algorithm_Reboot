import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0

for i in range(n-1, -1, -1):
    if arr[i] == x:
        cnt += 1
        n -= 1
        arr.pop()
    else:
        break
s = 0
e = n-1

while s < e:
    if (arr[s] + arr[e]) * 2 >= x:
        cnt += 1
        n -= 2
        e -= 1
        s += 1
    else:
        s += 1

cnt += n // 3
print(cnt)