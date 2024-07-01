n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))

# 이미 잘 서 있는 애들을 기준으로 잡고, 나머지를 옮기자
# 이미 잘 서 있는 애들이 최대일때 제일 적게 옮김

dp = [0 for i in range(n+1)]
for i in range(1, n+1):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))