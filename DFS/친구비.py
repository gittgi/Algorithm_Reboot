from collections import deque

n, m, k = map(int, input().split())
cost = [0] + list(map(int, input().split()))

arr = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)


def dfs(x):

    stack = deque()
    stack.append(x)
    while stack:
        x = stack.pop()
        for i in arr[x]:
            if not visited[i]:
                visited[i] = True
                friends.append(i)
                stack.append(i)


ans = 0
visited = [False] * (n+1)

for i in range(1, n+1):
    if not visited[i]:
        friends = []
        dfs(i)
        min_val = 10000
        if friends:
            for j in friends:
                min_val = min(cost[j], min_val)
        else:
            min_val = cost[i]
        ans += min_val

if ans > k:
    print("Oh no")
else:
    print(ans)       



