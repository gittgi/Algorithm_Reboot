n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for i in range(n)] for j in range(n)]
def recur(x, y, prev, cnt):
    if arr[x][y] <= prev:
        return cnt
    
    max_cnt = 0
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if 0 <= x+dx < n and 0 <= y+dy < n:
            if not visited[x+dx][y+dy]:
                visited[x+dx][y+dy] = True
                max_cnt =  max(max_cnt, recur(x+dx, y+dy, arr[x][y], cnt + 1))
                visited[x+dx][y+dy] = False
    
    return max_cnt


ans = 0
for i in range(n):
    for j in range(n):
        visited[i][j] = True
        ans = max(ans, recur(i, j, 0, 0))
        visited[i][j] = False
print(ans)

