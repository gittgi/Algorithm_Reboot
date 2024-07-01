from collections import deque
t = int(input())
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

for _ in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    tx, ty = map(int,input().split())

    visited = [[-1 for i in range(n)] for j in range(n)]
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = 0
    while q:
        x, y = q.popleft()

        if x == tx and y == ty:
            print(visited[x][y])
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if n > nx >= 0 and n > ny >= 0:
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    
    