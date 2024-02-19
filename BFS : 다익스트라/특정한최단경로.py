import sys
from collections import deque
input = sys.stdin.readline



n, e = map(int, input().split())

arr = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a].append((c, b))
    arr[b].append((c, a))

for i in arr:
    i.sort()

v1, v2 = map(int, input().split())

def dijkstra(start, end):
    visited = [float("inf")] * (n+1)
    visited[start] = 0
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        for d, i in arr[now]:
            if d + visited[now] < visited[i]:
                visited[i] = d + visited[now]
                q.append(i)
    
    return visited[end]

vv = dijkstra(v1, v2)
r1 = dijkstra(1, v1) + vv + dijkstra(v2, n)
r2 = dijkstra(1, v2) + vv + dijkstra(v1, n)

ans = min(r1, r2)
if ans == float("inf"):
    print(-1)
else:
    print(ans)
