import sys
from collections import deque
sys.stdin = open('K.in')
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



"""
1
4 5
*A***
*$*a.
**$**
**A**
0

1
5 9
*********
.......a*
***.*****
*$Ab*****
*********
0

1
5 5
aaaaa
aAAAa
aA$Aa
aAAAa
aaaaa
0
"""

"""
1
5 5
ABABA
AabaB
Bb$aB
AbabB
AABAa
0

3
5 17
*****************
.............**$*
*B*A*P*C**X*Y*.X.
*y*x*a*p**$*$**$*
*****************
cz
5 11
*.*********
*...*...*x*
*X*.*.*.*.*
*$*...*...*
***********
0
7 7
*ABCDE*
X.....F
W.$.G
V.$.H
U.$.J
T.....K
*SQPMI*
irony

1
6 3
***
...
*X*
*X*
*$*
***
x

1
2 2
$
$
0

1
3 3
aaa
a$a
aaa
0

4 5
1
*A***
*$*a.
**$**
**A**
0

1
5 11
*x*********
*...*...*.*
*X*.*.*.*.*
*$*...*...*
***********
0

1
3 4
****
*$A*
****
a

"""

'''
13
1182
92
62
192
231
60
116
300
83
59
40
22
195
112
1138
94
44
213
866
346
82
14
1218
1017
89
1111
164
1202
5
0
2
1
0
0
0
0
3
1
1
0
0
2
1
2
0
0
0
'''