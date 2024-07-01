# 가장 긴 증가하는 부분 수열과
# 가장 긴 증가하는 역방향 부분 수열의 합

n = int(input())
arr = list(map(int, input().split()))

dp = [1 for i in range(n)]

# dp[i] = arr[i]로 끝나는 증가 수열
for i in range(n):
    for j in range(i):
        if arr[j] >= arr[i]:
            continue
        dp[i] = max(dp[i], dp[j] + 1)

dp2 = [1 for i in range(n)]

# dp2[i] = 역방향 증가 수열
for i in range(n)[::-1]:
    for j in range(i+1, n):
        if arr[j] >= arr[i]:
            continue
        dp2[i] = max(dp2[i], dp2[j] + 1)

max_val = 0
for i in range(n):
    max_val = max(dp[i] + dp2[i], max_val)

# 자기 중복 제거
print(max_val - 1)