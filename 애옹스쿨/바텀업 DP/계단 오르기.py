n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

# dp[계단][연속] = 최대 값

dp = [[0 for i in range(2)] for j in range(n+2)]

for i in range(2, n+2):
    dp[i][0] = max(dp[i-2]) + arr[i - 2]
    dp[i][1] = dp[i-1][0] + arr[i-2]

print(max(dp[-1]))