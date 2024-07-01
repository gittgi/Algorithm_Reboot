n = int(input())
arr = [list(input()) for _ in range(n)]

visited = [[0 for i in range(n)] for j in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def recur(x, y):
    global cnt
    visited[x][y] = True
    cnt += 1


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == '1':
                if not visited[nx][ny]:
                    recur(nx, ny)

length = 0
ans = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == '1':
            if not visited[i][j]:
                length += 1
                cnt = 0
                recur(i, j)
                ans.append(cnt)

print(length)
ans.sort()
for i in ans:
    print(i)