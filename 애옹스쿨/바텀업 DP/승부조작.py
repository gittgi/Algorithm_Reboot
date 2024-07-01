n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0, 0, 0, 0] for i in range(n + 2)] for j in range(n + 1)]
# dp = (가로, 세로, 좌하대각선, 우하대각선)

for i in range(1, n+1):
    for j in range(1, n+1):
        if arr[i-1][j-1] != 1:
            dp[i][j] = [0, 0, 0, 0]
        else:
            dp[i][j] = [dp[i][j-1][0] + 1, dp[i-1][j][1] + 1, dp[i-1][j-1][2] + 1, dp[i-1][j+1][3] + 1]


for i in dp:
    print(i)

        