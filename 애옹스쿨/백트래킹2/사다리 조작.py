n, m, h = map(int, input().split())
arr = [[0 for j in range(n+1)] for i in range(h+1)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[a][b+1] = -1

empty = []
for i in range(1, h+1):
    for j in range(1, n):
        if arr[i][j] == 0 and arr[i][j+1] == 0:
            empty.append((i, j))

def check():
    for start in range(1, n+1):
        k = start
        for i in range(1, h+1):
            k += arr[i][k]
        if start != k:
            return False
        
    return True
        
min_val = float("inf")


def recur(cur, cnt):
    global min_val
    if cnt > 3 or cnt > min_val:
        return
    if cur == len(empty):
        if check():  # 매번 체크하면 시간 초과니까, 마지막에만 한번 체크하기
            min_val = min(min_val, cnt)
        return
    
    x, y = empty[cur]
    # 선 그을 수 있으면 긋기
    if arr[x][y] == 0 and arr[x][y+1] == 0:
        arr[x][y] = 1
        arr[x][y+1] = -1
        recur(cur + 1, cnt + 1)
        arr[x][y] = 0
        arr[x][y+1] = 0

    # 선 안긋기
    recur(cur + 1, cnt)

recur(0, 0)
if min_val == float("inf"):
    print(-1)
else:
    print(min_val)
    
    
    

    




