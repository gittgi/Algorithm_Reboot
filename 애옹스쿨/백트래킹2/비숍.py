n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

visited_r = [0 for _ in range(2*n - 1)]
visited_l = [0 for _ in range(2*n - 1)]
max_val = [0, 0]
def recur(x, y, color, cnt):
    if y >= n:
        x += 1
        y = 0
    
    if x == n:
        if max_val[color] < cnt:
            max_val[color] = cnt
        return
    
    if (x + y) % 2 != color:
        recur(x, y+1, color, cnt)
        return 
    
    if arr[x][y] == 0:
        recur(x, y+1, color, cnt)
        return
    
    # 놓을 수 있으면 놓는다.
    if visited_l[x - y - 1 + n] == 0 and visited_r[x+y] == 0:
        visited_l[x - y - 1 + n] = 1
        visited_r[x+y] = 1
        recur(x, y+1, color, cnt+1)
        visited_l[x - y - 1 + n] = 0
        visited_r[x+y] = 0
    
    # 놓지 않는다.
    recur(x, y+1, color, cnt)

recur(0, 0, 0, 0)
recur(0, 0, 1, 0)

print(sum(max_val))
