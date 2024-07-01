n, k = map(int, input().split())
arr = []
for i in range(n):
    w, v = map(int, input().split())
    arr.append((w, v))

# 
# def recur(cur, weight):
#     if weight > k:
#         return -10000000
    
#     if cur == n:
#         return 0
    
#     if dp[cur][weight] != -1:
#         return dp[cur][weight]


#     # cur : 현재 물건
#     dp[cur][weight] = max(recur(cur+1, weight + arr[cur][0]) + arr[cur][1], recur(cur+1, weight))
#     return dp[cur][weight]


dp = [[0 for i in range(200010)] for j in range(n+1)]
for i in range(n+1):
    for j in range(200010):
        if j > k:
            dp[i][j] = -100000000

for i in range(n)[::-1]:
    for j in range(100001):
        dp[i][j] = max(dp[i+1][j+arr[i][0]] + arr[i][1], dp[i+1][j])


print(dp[0][0])