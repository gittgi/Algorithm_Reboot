from collections import deque

n, m = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(n)]



def bfs(arr):
    q = deque()
    
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        if n > x + dx >= 0 and m > y + dy >= 0:
                            if visited[x+dx][y+dy] == 0:
                                if arr[x+dx][y+dy] == 0:
                                    q.append((x+dx, y+dy))
                                    visited[x+dx][y+dy] = 1
                                    cnt += 1

    return cnt
            
        


empty = []
zero = -3
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            empty.append((i, j))
            zero += 1


total = 64
for i in range(len(empty) - 2):
    for j in range(i+1, len(empty) - 1):
        for k in range(j+1, len(empty)):
            xi, yi = empty[i]
            xj, yj = empty[j]
            xk, yk = empty[k]
            arr[xi][yi] = 1
            arr[xj][yj] = 1
            arr[xk][yk] = 1
            total = min(total, bfs(arr))
            arr[xi][yi] = 0
            arr[xj][yj] = 0
            arr[xk][yk] = 0

print(zero - total)
