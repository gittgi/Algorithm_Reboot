n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

cameras = []

for i in range(n):
    for j in range(m):
        if 1 <= arr[i][j] <= 5:
            cameras.append((i, j, arr[i][j]))

ans = m * n

def recur(cur):
    global ans
    if cur == len(cameras):
        cnt = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    cnt += 1
        ans = min(cnt, ans)
        return
    x, y, type = cameras[cur]

    if type == 1:
        for d in range(4):
            gamsi(d, x, y, 10)
            recur(cur + 1)
            gamsi(d, x, y, -10)
    elif type == 2:
        for d in range(2):
            gamsi(d, x, y, 10)
            gamsi(d + 2, x, y, 10)
            recur(cur + 1)
            gamsi(d , x, y, -10)
            gamsi(d + 2, x, y, -10)
    elif type == 3:
        for d in range(4):
            gamsi(d, x, y, 10)
            gamsi((d+1) % 4, x, y, 10)
            recur(cur + 1)
            gamsi(d, x, y, -10)
            gamsi((d+1) % 4, x, y, -10)
    elif type == 4:
        for d in range(4):
            gamsi(d, x, y, 10)
        for d in range(4):
            gamsi(d, x, y, -10)
            recur(cur + 1)
            gamsi(d, x, y, 10)
        for d in range(4):
            gamsi(d, x, y, -10)
    elif type == 5:
        for d in range(4):
            gamsi(d, x, y, 10)
        recur(cur + 1)
        for d in range(4):
            gamsi(d, x, y, -10)


def gamsi(direction, x, y, do):
    if direction == 1:
        for j in range(y+1, m):
            if arr[x][j] == 6:
                break
            if 1 <= arr[x][j] <= 5:
                continue
            arr[x][j] += do
    elif direction == 3:
        for j in range(y-1, -1, -1):
            if arr[x][j] == 6:
                break
            if 1 <= arr[x][j] <= 5:
                continue
            arr[x][j] += do
        
    elif direction == 2:
        for i in range(x+1, n):
            if arr[i][y] == 6:
                break
            if 1 <= arr[i][y] <= 5:
                continue
            arr[i][y] += do
    
    else:
        for i in range(x-1, -1, -1):
            if arr[i][y] == 6:
                break
            if 1 <= arr[i][y] <= 5:
                continue
            arr[i][y] += do
    




recur(0)
print(ans)