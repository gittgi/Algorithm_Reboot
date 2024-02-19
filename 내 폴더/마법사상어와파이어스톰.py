from collections import deque
import sys
input = sys.stdin.readline


n, q = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(2**n)]

seq = list(map(int, input().split()))


def rotate(x, y, s):
    rep = [[0] * (2**s) for _ in range(2**s)]
    for i in range(2**s):
        for j in range(2**s):
            rep[j][(2**s)-i-1] = arr[i+x][j+y]
    
    for i in range(2**s):
        for j in range(2**s):
            arr[i+x][j+y] = rep[i][j]
    



def melt(x, y):
    cnt = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= x+dx < 2**n and 0 <= y+dy < 2**n:
            if arr[x+dx][y+dy] >= 1:
                cnt += 1
    if cnt < 3:
        to_melt.append((x, y))



for t in seq:

    for i in range(0, 2**n, 2**t):
        for j in range(0, 2**n, 2**t):
            rotate(i, j, t)

    to_melt = deque()
    for i in range(2**n):
        for j in range(2**n):
            if arr[i][j] >= 1:
                melt(i, j)
    
    for x, y in to_melt:
        arr[x][y] -= 1
    
    to_melt.clear()

            

total = 0
max_val = 0
visited = [[0] * (2**n) for _ in range(2**n)]

def bfs(x, y):
    cnt = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= x+dx < 2**n and 0 <= y+dy < 2**n:
                if arr[x+dx][y+dy] >= 1 and visited[x+dx][y+dy] == 0:
                    q.append((x+dx, y+dy))
                    visited[x+dx][y+dy] = 1
                    cnt += 1
    
    return cnt

for i in range(2**n):
    for j in range(2**n):
        if arr[i][j] >= 1:
            total += arr[i][j]
            if visited[i][j] == 0:
                max_val = max(max_val, bfs(i, j))


print(total)
print(max_val)
   


