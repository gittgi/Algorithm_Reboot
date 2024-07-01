from collections import deque

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()
tomato = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))
        elif arr[i][j] == 0:
            tomato += 1

visited = [[False for i in range(m)] for j in range(n)]
day = 0
rot = 0
while q:
    day += 1
    for t in range(len(q)):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if n > nx >= 0 and m > ny >= 0:
                if arr[nx][ny] == 0:
                    if not visited[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        rot += 1
if tomato == rot:
    print(day-1)
else:
    print(-1)
                        
