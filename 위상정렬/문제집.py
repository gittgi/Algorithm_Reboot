from heapq import heappop, heappush
import sys
input = sys.stdin.readline


n, m = map(int, input().split())

jinip = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    jinip[b] += 1


def topology():
    q = []
    result = []
    for i in range(1, n+1):
        if jinip[i] == 0:
            heappush(q, i)
    
    while q:
        x = heappop(q)
        result.append(x)
        for i in graph[x]:
            jinip[i] -= 1
            if jinip[i] == 0:
                heappush(q, i)

    print(*result)

topology()