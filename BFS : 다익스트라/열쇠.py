import sys
from collections import deque
input = sys.stdin.readline

upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V','W','X','Y','Z']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def bfs(x, y):
    global docs
    q = deque()
    q.append((x, y))
    

    keys = set()
    obstacle = set()
    if arr[x][y] in lower:
        keys.add(arr[x][y])
        arr[x][y] = "."
        visited[x][y] = 1
    elif arr[x][y] == '$':
        docs += 1
        arr[x][y] = "."
        visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if h > x+dx >= 0 and w > y+dy>=0:
                if arr[x+dx][y+dy] != '*':
                    if visited[x+dx][y+dy] == 0:
                        # 문서
                        if arr[x+dx][y+dy] == '$':
                            docs += 1
                      
                            arr[x+dx][y+dy] = '.'
                            visited[x+dx][y+dy] = 1
                            q.append((x+dx, y+dy))
                        # 열쇠
                        elif arr[x+dx][y+dy] in lower:
                            keys.add(arr[x+dx][y+dy])
                            arr[x+dx][y+dy] = '.'
                            visited[x+dx][y+dy] = 1
                            q.append((x+dx, y+dy))
                        # 장애물
                        elif arr[x+dx][y+dy] in upper:
                            obstacle.add(arr[x+dx][y+dy])
                            visited[x+dx][y+dy] = 1
                        # 평지
                        else:
                            visited[x+dx][y+dy] = 1
                            q.append((x+dx, y+dy))
    
    return keys, obstacle

def open_door():
    for i in range(h):
        for j in range(w):
            if arr[i][j].lower() in keys:
                arr[i][j] = '.'                       

def get_start():
    start_point = set()
   
    for i in range(h):
        if arr[i][0] == '.' or arr[i][0] in lower or arr[i][0] == '$':
            start_point.add((i, 0))
        elif arr[i][0] in upper:
            obstacle.add(arr[i][0])

        if arr[i][w-1] == '.' or arr[i][w-1] in lower or arr[i][w-1] == '$':
            start_point.add((i, w-1))
        elif arr[i][w-1] in upper:
            obstacle.add(arr[i][w-1])

    for j in range(w):
        if arr[0][j] == '.' or arr[0][j] in lower or arr[0][j] == '$':
            start_point.add((0, j))
        elif arr[0][j] in upper:
            obstacle.add(arr[0][j])

        if arr[h-1][j] == '.' or arr[h-1][j] in lower or arr[h-1][j] == '$':
            start_point.add((h-1, j))
        elif arr[h-1][j] in upper:
            obstacle.add(arr[h-1][j])
    return start_point





t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    arr = list(list(input().strip()) for _ in range(h))
    keys = list(input().strip())
    docs = 0
    again = True
    open_door()
    while again:
        keys = set()
        obstacle = set()
        start_point = get_start()
        # print(start_point)
        visited = [[0] * w for _ in range(h)]
        for x, y in start_point:
            if visited[x][y] == 0:
           
                temp_keys, temp_obstacle = bfs(x, y)
                keys = keys | temp_keys
                obstacle = temp_obstacle | obstacle
        # print(keys)
        for i in obstacle:
            if i.lower() in keys:
                open_door()

                again = True
                break
        else:
            again = False
    # print(arr)
    print(docs)


# 입구가 열쇠이거나 하는 엣지 케이스들을 생각했어야 함...
# 아니면 .으로 패딩을 주고 들락날락 할 수 있게 하는 방법이 더 좋았을듯