import sys
input = sys.stdin.readline
from collections import deque, defaultdict

n, m = map(int, input().split())

arr = list(list(input().rstrip()) for _ in range(n))

group = defaultdict(int)

def bfs(x, y, key_num):
    q = deque()
    q.append((x, y))
  
 
    arr[x][y] = key_num
    cnt = 1
    while q:
        x, y = q.popleft()

        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            if n > x +dx >= 0 and m > y+dy>= 0:
                if arr[x+dx][y+dy] == '0':
                    cnt += 1
                    arr[x+dx][y+dy] = key_num
                    q.append((x+dx, y+dy))

    group[key_num] = cnt 
   
key_num = -1
for i in range(n):
    for j in range(m):
       
        if arr[i][j] == '0':
            bfs(i ,j, key_num)
            key_num -= 1

# print(arr)

for i in range(n):
    for j in range(m):
       
        if arr[i][j] == '1':
            cnt = 1
            temp_groups = set()
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                if n > i +dx >= 0 and m > j+dy>= 0:
                    if arr[i+dx][j+dy] != '1':
                        temp_groups.add(arr[i+dx][j+dy])
            
            for k in temp_groups:
                cnt += group[k]
            arr[i][j] = str(cnt %  10)

for i in range(n):
    for j in range(m):
        if int(arr[i][j]) < 0:
            arr[i][j] = '0'

for i in arr:
    
    print(''.join(i))

print(group)