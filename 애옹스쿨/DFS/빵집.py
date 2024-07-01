import sys
input = sys.stdin.readline

r, c = map(int, input().split())

arr = [list(input()) for _ in range(r)]

# 최대한 위로 붙여서 파이프라인을 놓으면 될까?
visited = [[False for i in range(c)] for j in range(r)]

dx = [1, 0, -1]

def dfs(x, y):
    stack = []
    stack.append((x, y))

    while stack:
        x, y = stack.pop()
        visited[x][y] = True
        if y == c- 1:
            return True
        for i in dx:
            nx = x + i
            ny = y + 1
            if 0 <= nx < r:
                if arr[nx][ny] == "." and not visited[nx][ny]:
                    stack.append((nx, ny))
        
    return False


            



cnt = 0
for x in range(r):
    if dfs(x, 0):
        cnt += 1

print(cnt)

