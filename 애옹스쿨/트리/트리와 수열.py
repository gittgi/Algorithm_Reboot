import sys
sys.setrecursionlimit(100010)
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


sub = [0 for _ in range(n+1)]

def dfs(x, prv):
    sub[x] = 1

    for i in arr[x]:
        if i == prv:
            continue

        dfs(i, x)
        sub[x] += sub[i]

dfs(1, -1)
lst = []
for i in range(2, n+1):
    lst.append((n - sub[i]) * sub[i])

lst.sort()

vals = list(map(int, input().split()))

vals.sort(reverse=True)

ans = 0
for i in range(n-1):
    ans += ((vals[i] * lst[i]))

print(ans % ((10 ** 9) + 7))