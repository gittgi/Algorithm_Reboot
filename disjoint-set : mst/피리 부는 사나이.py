import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# from collections import deque


def find(x, y):
    if (x, y) == parent[x][y]:
        return x, y
    
    else:

        parent[x][y] = find(parent[x][y][0], parent[x][y][1])
        return parent[x][y]
    

def union(x1, y1, x2, y2):
    x1, y1 = find(x1, y1)
    x2, y2 = find(x2, y2)
    if (x1, y1) == (x2, y2):
        return
    else:
        if rank[x1][y1] > rank[x2][y2]:
            parent[x2][y2] = (x1, y1)
        elif rank[x1][y1] < rank[x2][y2]:
            parent[x1][y1] = (x2, y2)
        else:
            parent[x1][y1] = (x2, y2)
            rank[x2][y2] += 1

def dfs(x, y): 
    old_x = x
    old_y = y

    if arr[x][y] == "U":
        x -= 1
    elif arr[x][y] == "D":
        x += 1
    elif arr[x][y] == "L":
        y -= 1
    else:
        y += 1

    

    if find(x, y) == find(old_x, old_y): # 만약 현재칸과 다음칸의 그룹이 같다면
        return
    union(x, y, old_x, old_y) # 다음칸과 지금칸의 부모를 일치 시켜준다
    dfs(x, y) # 다음칸에서 계속


n, m = map(int, input().split())

arr = [list(input().strip()) for _ in range(n)]

parent = [[0] * m for _ in range(n)]

rank = [[1] * m for _ in range(n)]

ans = set()

for i in range(n):
    for j in range(m):
        parent[i][j] = (i, j)

for i in range(n):
    for j in range(m):
        if find(i, j) == (i, j):
            dfs(i, j)

for i in range(n):
    for j in range(m):
        if find(i, j) == (i, j):
            ans.add((i,j))

print(len(ans))
