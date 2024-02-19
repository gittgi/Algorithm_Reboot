from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, r, q = map(int, input().split())
arr = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [False] * (n+1)
visited[r] = True
dp = [1] * (n+1)

def dfs(x):
    for i in arr[x]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
            dp[x] += dp[i]

    


dfs(r)


for _ in range(q):
    i = int(input())
    print(dp[i])
