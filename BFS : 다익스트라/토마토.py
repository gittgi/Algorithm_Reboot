import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

arr  = list(list(map(int, input().split())) for _ in range(n))

rotten = []


for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            rotten.append((i,j))
           


def bfs():
    q = deque(rotten)

    while q:
        x, y = q.popleft()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            if n > x+dx >= 0 and m > y+dy >= 0:
                if arr[x+dx][y+dy] == 0:
                    arr[x+dx][y+dy] = arr[x][y] + 1
                    q.append((x+dx, y+dy))

    max_val = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                print(-1)
                return
            else:
                max_val = max(max_val, arr[i][j])
    
    print(max_val - 1)

bfs()