from collections import deque

n = int(input())

arr = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [0] * (n+1)
visited[1] = -1

def dfs(x):

    stack = deque()
    stack.append(x)

    while stack:
        x = stack.pop()
        for i in arr[x]:
            if visited[i] == 0:
                visited[i] = x
                stack.append(i)

dfs(1)
for i in range(2, n+1):
    print(visited[i])    