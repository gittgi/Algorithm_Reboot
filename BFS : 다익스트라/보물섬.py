from collections import deque

n , m = map(int,input().split())

arr = [list(input()) for _ in range(n)]

def bfs(x, y):

    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    temp = 0
    while q:
        px, py = q.popleft()

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = px + dx, py + dy
            if n > nx >= 0 and m > ny >= 0:
                if arr[nx][ny] == 'L':
                    if visited[nx][ny] == -1:
                        q.append((nx, ny))
                        visited[nx][ny] = visited[px][py] + 1
                        temp = max(temp, visited[px][py] + 1)
    return temp
    
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            visited = [[-1] * m for _ in range(n)]
            ans = max(ans, bfs(i, j))

print(ans)