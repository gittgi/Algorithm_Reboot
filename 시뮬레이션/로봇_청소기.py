def move(x, y, d):

    global cnt
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    here = arr[x][y]
    if here == 0:
        arr[x][y] = -1
        cnt += 1
      
    
    is_near_uncleared = False
    for dx, dy in [(1,0), (0, 1), (-1, 0), (0, -1)]:
   
        if 0 <= x+dx < N and 0 <= y+dy < M:
            if arr[x+dx][y+dy] == 0:
                is_near_uncleared = True
        
    if is_near_uncleared:
        d = (d - 1) % 4
        dx, dy = direction[d]
        if 0 <= x+dx < N and 0 <= y+dy < M:
            if arr[x+dx][y+dy] == 0:
                x += dx
                y += dy
              
    else:
        dx, dy = direction[d]
        if 0 <= x-dx < N and 0 <= y-dy < M:
            if arr[x-dx][y-dy] != 1:
                x -= dx
                y -= dy
              
            else:
             
                return -1, -1, d
    
    return x, y, d


N, M = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

while x != -1 and y != -1:
    x, y, d = move(x, y, d)
  
print(cnt)








