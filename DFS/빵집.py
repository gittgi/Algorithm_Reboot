from collections import deque

R, C = map(int, input().split())

arr = [list(input()) for _ in range(R)]

visited = [[False] * C for _ in range(R)]

cnt = 0

def dfs(i):
    global cnt
    stack = deque()
    stack.append((i, 0))

    while stack:
  
        x, y = stack.pop()
        visited[x][y] = True

        if y == C - 1:
            cnt += 1
      
            break

        for dx, dy in [(1, 1), (0, 1), (-1, 1)]:
      
            if R > x+dx >= 0 and C > y+dy >= 0:
                if arr[x+dx][y+dy] == '.':
                    if not visited[x+dx][y+dy]:
                        stack.append((x+dx, y+dy))
                   


for i in range(R):
    dfs(i)

print(cnt)