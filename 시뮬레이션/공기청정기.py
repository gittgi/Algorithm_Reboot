def diffusion(x, y):
    cnt = 0
    if (x, y) not in [(gx1, gy1), (gx2, gy2)]:
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if r > x + dx >= 0 and c > y + dy >= 0:
                if (x + dx, y + dy) not in [(gx1, gy1), (gx2, gy2)]:
                    copy_arr[x+dx][y+dy] += (arr[x][y] // 5)
                    cnt += 1
                

        arr[x][y] = arr[x][y] - ((arr[x][y] // 5) * cnt)


def circulation_up(gx, gy):
    for x in range(gx-1, 0, -1):
        arr[x][0] = arr[x-1][0]
    for y in range(0, c-1):
        arr[0][y] = arr[0][y+1]
    
    for x in range(0, gx):
        arr[x][c-1] = arr[x+1][c-1]
    for y in range(c-1, 0, -1):
        arr[gx][y] = arr[gx][y-1]
    
    arr[gx][gy] = -1
    arr[gx][gy+1] = 0
    

def circulation_down(gx, gy):
    for x in range(gx+1, r-1):
        arr[x][0] = arr[x+1][0]
    for y in range(0, c-1):
        arr[r-1][y] = arr[r-1][y+1]
    
    for x in range(r-1, gx, -1):
        arr[x][c-1] = arr[x-1][c-1]
    for y in range(c-1, 0, -1):
        arr[gx][y] = arr[gx][y-1]

    arr[gx][gy] = -1
    arr[gx][gy+1] = 0
  


r, c, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(r)]




for i in range(r):
    if arr[i][0] == -1:
            gx1 = i-1
            gx2 = i
            gy1 = 0
            gy2 = 0
   



while t > 0:
    t -= 1
    copy_arr = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            diffusion(x, y)
    for x in range(r):
        for y in range(c):
            arr[x][y] += copy_arr[x][y] 
    

    circulation_up(gx1, gy1)
    circulation_down(gx2, gy2)
    


ans = 0



for i in range(r):
    for j in range(c):
       ans += arr[i][j]

ans += 2



print(ans)

