n = int(input())

# dp[n] == 2 * n을 채우는 경우의 수

# 1 * 2 로 시작하거나, 2 * 2 로 시작
dp = [0 for i in range(n+1)]

dp[0] = 1
dp[1] = 1


# 1 * 2를 붙이거나 2 * 2를 붙임
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]


print(dp[n] % 10007)