import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
jinip = [0] * (n+1)


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    jinip[b] += 1


print(graph)
print(jinip)

def topology():
    q = deque()
    result = []

    for i in range(1, n+1):
        if jinip[i] == 0:
            q.append(i)
    
    while q:
        x = q.popleft()
        result.append(x)
        for i in graph[x]:
            jinip[i] -= 1
            if jinip[i] == 0:
                q.append(i)
        

    
    print(*result)

topology()