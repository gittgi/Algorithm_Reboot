from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

q = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def find_air():
    q = deque()
    q.append((0, 0))
    visited = [[False for i in range(m)] for j in range(n)]
    visited[0][0] = True
    air = deque()
    air.append((0, 0))
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            if n > nx >=0 and m > ny >= 0:
                if arr[nx][ny] == 0 and visited[nx][ny] == False:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    air.append((nx, ny))

    return air

time = 0
while True:
    time += 1
    q = find_air()
    left = 0
    for x, y in q:
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            if n > nx >=0 and m > ny >= 0:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    left += 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1

    if cnt == 0:
        print(time)
        print(left)
        break 