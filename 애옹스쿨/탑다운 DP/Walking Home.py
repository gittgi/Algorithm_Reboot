t = int(input())

# prev: 0 우로 이동, 1 하로 이동
def recur(x, y, curve, prev):
    if x == n or y == n:
        return 0
    
    if arr[x][y] == 'H':
        return 0

    if curve > k:
        return 0
    
    if x == n-1 and y == n-1:
        return 1
    
    if dp[x][y][curve][prev] != -1:
        return dp[x][y][curve][prev]

    cnt = 0
    # 우로 이동 중일 때
    if prev == 0:
        # 그대로 우로 이동
        cnt += recur(x, y+1, curve, 0)
        # 하로 변경
        cnt += recur(x+1, y, curve + 1, 1)
    
    else:
        # 우로 변경
        cnt += recur(x, y+1, curve + 1, 0)
        # 그대로 하로 이동
        cnt += recur(x+1, y, curve, 1)

    dp[x][y][curve][prev] = cnt
    return cnt

    



for _ in range(t):
    n, k = map(int, input().split())
    arr = [list(input()) for i in range(n)]
    dp = [[[[-1 for i in range(2)] for j in range(k+1)] for l in range(n)] for q in range(n)]
    ans = recur(1, 0, 0, 1) + recur(0, 1, 0, 0)
    print(ans)
    