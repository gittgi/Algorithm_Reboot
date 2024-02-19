import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

arr  = list(list(list(map(int, input().split())) for _ in range(n)) for _ in range(h))

rotten = []

for l in range(h):
    for i in range(n):
        for j in range(m):
            if arr[l][i][j] == 1:
                rotten.append((l, i, j))
             


def bfs():
    q = deque(rotten)

    while q:
        z, x, y = q.popleft()
        for dz, dx, dy in [(0,1,0),(0,-1,0),(0,0,1),(0,0,-1), (1,0,0), (-1,0,0)]:
            if h>z+dz>=0 and n > x+dx >= 0 and m > y+dy >= 0:
                if arr[z+dz][x+dx][y+dy] == 0:
                    arr[z+dz][x+dx][y+dy] = arr[z][x][y] + 1
                    q.append((z+dz,x+dx, y+dy))

    max_val = 0
    for l in range(h):
        for i in range(n):
            for j in range(m):
                if arr[l][i][j] == 0:
                    print(-1)
                    return
                else:
                    max_val = max(max_val, arr[l][i][j])
    
    print(max_val - 1)

bfs()