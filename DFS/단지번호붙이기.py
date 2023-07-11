from collections import deque

n = int(input())

arr = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def dfs(x, y):
    stack = deque()
    stack.append((x, y))
    visited[x][y] = True
    cnt = 1
    while stack:
        x, y = stack.pop()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if n > nx >= 0 and n > ny >= 0:
                if arr[nx][ny] == '1':
                    if not visited[nx][ny]:
                        cnt += 1
                        visited[nx][ny] = True
                        stack.append((nx, ny))

    return cnt

ans = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == '1':
            if not visited[i][j]:
                ans.append(dfs(i, j))

print(len(ans))
for i in ans:
    print(i) 
