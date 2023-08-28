import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

jinip = [0] * (n+1)

for _ in range(m):
    arr = list(map(int, input().split()))
    for i in range(arr[0] - 1):
        a, b  = arr[i + 1], arr[i + 2]
        graph[a].append(b)
        jinip[b] += 1
    

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
        
    
    if len(result) == n:
        for i in result:
            print(i)
    else:
        print(0)

topology()