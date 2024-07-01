from collections import deque
n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    
    q = deque()
    q.append((x, y, 0))
    max_val = 0
    visited = [[False for _ in range(m)] for i in range(n)]
    visited[x][y] = True
    while q:
        x, y, d = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if n > nx >= 0 and m > ny >= 0:
                if arr[nx][ny] == "L":
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny, d + 1))
                        max_val = max(max_val, d+1)
    
    return max_val

max_val = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == "L":
            max_val = max(max_val, bfs(i, j))

print(max_val)
