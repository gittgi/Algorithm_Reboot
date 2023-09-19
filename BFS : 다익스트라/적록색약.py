import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

arr = list(list(input().rstrip()) for _ in range(n))
print(arr)
visited = [[0] * n for _ in range(n)]

def bfs(x, y, color):

    q = deque()
    q.append((x, y))
    visited[x][y] = 1
   
    while q:
        x, y = q.popleft()

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if n > x+dx >=0 and n > y+dy >=0:
                if visited[x+dx][y+dy] == 0:
                    if arr[x+dx][y+dy] == color:
                        visited[x+dx][y+dy] = 1
                
                        q.append((x+dx, y+dy))
   
ans_1 = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j, arr[i][j])
            ans_1 += 1

visited = [[0] * n for _ in range(n)]
ans_2 = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == "R":
            arr[i][j] = "G"

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j, arr[i][j])
            ans_2 += 1

print(ans_1, ans_2)