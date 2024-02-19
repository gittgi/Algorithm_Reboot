import sys
from collections import deque
input = sys.stdin.readline


n, m, goal = map(int, input().split())


graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((d, b))
 
for i in graph:
    i.sort()

def dijkstra(start, end):
    if start == end: return 0
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    q = deque()
    q.append((start))

    while q:
        a = q.popleft()
        for d, b in graph[a]:
            if dist[b] > dist[a] + d:
                dist[b] = dist[a] + d
                q.append(b)

    return dist[end]

max_val = 0
for i in range(1, n + 1):
    go = dijkstra(i, goal)
    come = dijkstra(goal, i)
    max_val = max(max_val, go + come)

print(max_val)

