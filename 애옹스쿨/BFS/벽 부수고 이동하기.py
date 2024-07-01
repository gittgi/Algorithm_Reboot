from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[[-1, -1] for i in range(m)] for j in range(n)]

q = deque()

# x, y, 벽깬 횟수
q.append((0, 0, 0))
visited[0][0] = [1, 1]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while q:
    x, y, cnt = q.popleft()


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if n > nx >= 0 and m > ny >= 0:
            if arr[nx][ny] == "0":
                if visited[nx][ny][cnt] == -1:
                    visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                    q.append((nx, ny, cnt))
            
            else:
                if cnt == 0:
                    if visited[nx][ny][cnt+1] == -1:
                        visited[nx][ny][cnt + 1] = visited[x][y][cnt] + 1
                        q.append((nx, ny, cnt + 1))


a, b = visited[-1][-1] 
if a == -1 and b == -1:
    print(-1)
elif a == -1:
    print(b)
elif b == -1:
    print(a)
else:
    print(min(a, b))



