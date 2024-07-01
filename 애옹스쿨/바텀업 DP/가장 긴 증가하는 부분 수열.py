n = int(input())
arr = list(map(int, input().split()))

dp = [1 for i in range(n)]

# dp[i] = arr[i]로 끝나는 수열
for i in range(n):
    for j in range(i):
        if arr[j] >= arr[i]:
            continue
        dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))