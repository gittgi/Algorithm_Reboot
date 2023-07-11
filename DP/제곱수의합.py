# dp[N]의 값이 항상 최소 임을 기억
# 따라서 dp[N-x] 역시 최소임을 기억
# 그렇게 되면 적절한 제곱수인 x가 있다면, 그것을 빼준 dp[N-x] 역시 최선의 값임을 기억
# 이후 x 값을 더해주는 횟수인 +1 만 해주면 답


n = int(input())

dp = [float("inf")] * (n+1)
temp = []
for i in range(2, n+1):
    
    if int(i**(1/2)) ** 2 == i:
        temp.append(i)
        dp[i] = 1
    else:
        for j in temp:
            dp[i] = min(dp[i], dp[j] + dp[i-j])
    
print(dp[-1])