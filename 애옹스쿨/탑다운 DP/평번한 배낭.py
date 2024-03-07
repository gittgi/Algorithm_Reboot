n, k = map(int, input().split())
arr = []
for i in range(n):
    w, v = map(int, input().split())
    arr.append((w, v))

dp = [[-1 for i in range(100010)] for j in range(n)]

def recur(cur, weight):
    if weight > k:
        return -10000000
    
    if cur == n:
        return 0
    
    if dp[cur][weight] != -1:
        return dp[cur][weight]

    dp[cur][weight] = max(recur(cur+1, weight + arr[cur][0]) + arr[cur][1], recur(cur+1, weight))
    return dp[cur][weight]

print(recur(0, 0))