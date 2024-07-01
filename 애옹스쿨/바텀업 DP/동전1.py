n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

# dp[i] = i를 만드는 경우의 수
# dp[10] = dp[9] + dp[8] + dp[2]
# 그런데 dp[9] 에도 dp[2] 가 포함 -> 경우의 수 중복
dp = [0 for i in range(k+1)]    
dp[0] = 1

# 중복 제거를 위해서, 먼저 1로만 다 만들어보고, 그 뒤에 2만 추가해서 경우의 수를 늘려주고 그 다음 5..를 반복
for val in arr:
    for i in range(1, k+1):
        if i -val >= 0:
            dp[i] += dp[i - val]

print(dp[k])
