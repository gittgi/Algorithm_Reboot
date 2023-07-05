N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1, -1, -1] for _ in range(N)]

dp[0] = arr[0]

for i in range(1, N):
    dp[i][0] = arr[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = arr[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = arr[i][2] + min(dp[i-1][1], dp[i-1][0])





print(min(dp[-1]))

# 무엇을 더해줄 것인가에 대한 고민...
# 다음 숫자가 무조건 더해진다고 쳤을 때, 그전까지의 최솟값을 생각하는게 핵심...