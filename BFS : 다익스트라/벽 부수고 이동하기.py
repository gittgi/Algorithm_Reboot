import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

arr = [list(input().strip()) for _ in range(n)]

visited = [[[0, 0] for _ in range(m)] for _ in range(n)] # [벽 부순 애, 벽 안부순 애]
visited[0][0] = [1, 1]

def bfs():
    q = deque()
    q.append((0,0,1))

    
    while q:
        x, y, power = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if n > x+dx>= 0 and m > y+dy >= 0:
                if power: # 벽을 안부순 애
                    if not visited[x+dx][y+dy][power]: # 벽 안부순 애가 방문한 적 없으면
                        if arr[x+dx][y+dy] == '0': # 벽이 아닌 경우에는
                            visited[x+dx][y+dy][power] = visited[x][y][power] + 1
                            q.append((x+dx, y+dy, power))
                        else: # 벽인 경우에는
                            visited[x+dx][y+dy][0] = visited[x][y][power] + 1
                            q.append((x+dx, y+dy, 0))
               
                else: #벽 부순 애
                    if not visited[x+dx][y+dy][power]: # 벽 부순 애가 방문한 적 없으면
                        if arr[x+dx][y+dy] == '0': # 벽이 아닌 경우에는
                            visited[x+dx][y+dy][power] = visited[x][y][power] + 1
                            q.append((x+dx, y+dy, power))
                       


bfs()


if visited[n-1][m-1][0] == 0 and visited[n-1][m-1][1] == 0:
    print(-1)
else:
    if visited[n-1][m-1][0] == 0:
        print(visited[n-1][m-1][1])
    elif visited[n-1][m-1][1] == 0:
        print(visited[n-1][m-1][0])
    else:
        print(min(visited[n-1][m-1]))

