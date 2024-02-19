from collections import deque

N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [False] * (N+1)

def dfs(p):

    stack = deque()
    stack.append(p)
    visited[p] = True
    while stack:
        now = stack.pop()
        for i in arr[now]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)

                

cnt = 0

for i in range(1, N+1):

    if not visited[i]:

        cnt += 1
       
        dfs(i)

print(cnt)