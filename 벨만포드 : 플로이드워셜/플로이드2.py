import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[float("inf")] * (n+1) for _ in range(n+1)]
prev = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] == float("inf"):
        graph[a][b] = c
        prev[a][b] = a
    else:
        if graph[a][b] > c:
            graph[a][b] = c
            prev[a][b] = a

for i in range(n+1):
    graph[i][i] = 0

def floyd_warshall():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist_ij = graph[i][j]
                dist_ik = graph[i][k]
                dist_kj = graph[k][j]

                if dist_ij > dist_ik + dist_kj:
                    graph[i][j] = dist_ik + dist_kj
                    prev[i][j] = prev[k][j]

def tracker(i, j, route):
  
    next = prev[i][j]
    if i == next:
        route.append(i)
        return route
    else:
        route.append(next)
        
        return tracker(i, next, route)


floyd_warshall()
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == float("inf"):
            graph[i][j] = 0
               
for i in range(1, n+1):
    print(*graph[i][1:])
    
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == 0:
            print(0)
        else:
            temp = tracker(i, j, [])
            ans = [len(temp)+ 1] + temp[::-1] + [j]
            print(*ans)
