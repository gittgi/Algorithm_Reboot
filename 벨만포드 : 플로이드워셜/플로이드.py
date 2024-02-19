import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[float("inf")] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] == float("inf"):
        graph[a][b] = c
    else:
        if graph[a][b] > c:
            graph[a][b] = c

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


floyd_warshall()
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == float("inf"):
            graph[i][j] = 0
               
for i in range(1, n+1):
    print(*graph[i][1:])


