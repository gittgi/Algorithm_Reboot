import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x, y):
    if parent[x][y] == (x, y):
        return (x, y)
    parent[x][y] = find(parent[x][y][0], parent[x][y][1])
    return parent[x][y]

def union(x1, y1, x2, y2):
    x1, y1 = find(x1, y1)
    x2, y2 = find(x2, y2)
    if (x1, y1) == (x2, y2):
        return
    if rank[x1][y1] > rank[x2][y2]:
        parent[x2][y2] = (x1, y1)
    elif rank[x1][y1] < rank[x2][y2]:
        parent[x1][y1] = (x2, y2)
    else:
        parent[x1][y1] = (x2, y2)
        rank[x2][y2] += 1

def dfs(x, y):
    if visited[x][y]:
        return
    visited[x][y] = True
    if arr[x][y] == "U":
        x -= 1
    elif arr[x][y] == "D":
        x += 1
    elif arr[x][y] == "L":
        y -= 1
    else:
        y += 1
    union(x, y, old_x, old_y)
    dfs(x, y)

n, m = map(int, input().split())

arr = [list(input().strip()) for _ in range(n)]

parent = [[(i, j) for j in range(m)] for i in range(n)]
rank = [[1] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

ans = set()

for i in range(n):
    for j in range(m):
        old_x, old_y = i, j
        if not visited[i][j]:
            dfs(i, j)

for i in range(n):
    for j in range(m):
        ans.add(find(i, j))

print(len(ans))
