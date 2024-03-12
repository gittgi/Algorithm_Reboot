n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for i in range(m)] for j in range(n)]

def recur(x, y, prev):
    if x == n or y == m or x == -1 or y == -1:
        return 0

    if arr[x][y] >= prev:
        return 0
    
    if x == n - 1 and y == m - 1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    

    dp[x][y] =  recur(x+1, y, arr[x][y]) + recur(x, y+1, arr[x][y]) + recur(x-1, y, arr[x][y]) + recur(x, y-1, arr[x][y])
    return dp[x][y]

print(recur(0, 0, 10010))