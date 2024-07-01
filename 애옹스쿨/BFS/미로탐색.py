from collections import deque

n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]
dist = [[-1 for _ in range(m)] for i in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = deque()
q.append((0, 0))
dist[0][0] = 1
while q:
    x, y = q.popleft()

    if x == n-1 and y == m-1:
        print(dist[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
    
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == "1":
                if dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))


