from collections import deque
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def bfs(x, y, rain):
    visited[x][y] = 1
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for dx, dy in [(1,0), (-1, 0), (0, 1), (0, -1)]:
            if n > x+dx >= 0 and n > y + dy >= 0:
                if visited[x+dx][y+dy] == 0:
                    if arr[x+dx][y+dy] > rain:
                        visited[x+dx][y+dy] = 1
                        q.append((x+dx, y+dy))

max_height = 0
for i in arr:
    max_height = max(max_height, max(i))


ans = 0

for rain in range(max_height):
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > rain and visited[i][j] == 0:
                bfs(i, j, rain)
                cnt += 1
    ans = max(ans, cnt)

print(ans)