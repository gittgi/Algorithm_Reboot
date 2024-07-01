from collections import deque

n, t = map(int, input().split())

arr = [(0, 0)]
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

graph = [[] for i in range(n+1)]
for i in range(len(arr)):
    x, y = arr[i]
    for j in range(len(arr)):
        nx, ny = arr[j]
        if abs(nx - x) <= 2 and abs(ny - y) <= 2:
            graph[i].append(j)

visited = [-1 for _ in range(n+1)]
q = deque()
q.append(0)
visited[0] = 0

while q:
    now = q.popleft()
    if arr[now][1] >= t:
        print(visited[now])
        break

    for i in graph[now]:
        if visited[i] == -1:
            q.append(i)
            visited[i] = visited[now] + 1

else:
    print(-1)


