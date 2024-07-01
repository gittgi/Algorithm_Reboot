t = int(input())


# dp[k][n][0] : n의 자리수 중 k가 되는 수 중 마지막 비트가 0
# dp[k][n][1] : n의 자리수 중 k가 되는 수 중 마지막 비트가 1

dp = [[[0 for i in range(2)] for j in range(102)] for l in range(102)]
dp[1][1] = [2, 1]
dp[2][1]= [0, 1]
for i in range(2, 102):
    dp[1][i] = [sum(dp[1][i-1]), dp[1][i-1][0]]

for i in range(2, 102):
    for j in range(2, 102):
        
        dp[i][j] = [sum(dp[i][j-1]), dp[i][j-1][0] + dp[i-1][j-1][1]]


# 패딩 조절
for _ in range(t):
    n, k = map(int,input().split())
    print(sum(dp[k+1][n-1]))

