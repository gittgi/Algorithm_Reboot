import sys

input = sys.stdin.readline

def move (x,y,d,s):
    direction=[(0, -1), ( -1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0) , (1, -1)]

    x = (x + direction[d-1][0] * s) % n
    y = (y + direction[d-1][1] * s) % n

    arr[x][y] += 1
    return x, y


def water(x, y):
    direction = [(1, -1), (-1, -1), (1, 1), (-1, 1)]
    cnt = 0
    for dx, dy in direction:
        if 0 <= x+dx < n and 0 <= y+dy < n:
            if arr[x+dx][y+dy] > 0:
                cnt += 1
    
    arr[x][y] += cnt

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

cloud_list = [(n-1, 0), (n-2, 1), (n-2, 0), (n-1, 1)]
disappear_list = []

for i in range(m):
    d, s = map(int, input().split())
    for x, y in cloud_list:
        nx, ny = move(x,y,d,s)
        disappear_list.append((nx, ny))
    
    
    for x, y in disappear_list:
        water(x, y)
   
    cloud_list = []
    for x in range(n):
        for y in range(n):
            if (x, y) not in disappear_list:
                if arr[x][y] >= 2:
                    arr[x][y] -= 2
                    cloud_list.append((x, y))
    disappear_list = []
 

ans = 0
for x in range(n):
    for y in range(n):
        ans += arr[x][y]
    

print(ans)
print(arr)
