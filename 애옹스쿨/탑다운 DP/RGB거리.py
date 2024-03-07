n = int(input())
arr = [0 for i in range(n)]
for i in range(n):
    a, b, c = map(int, input().split())
    arr[i] = (a, b, c)

dp = [[-1 for i in range(3)] for j in range(n)]

def recur(cur, prv):
    if cur == n:
        return 0
    
    if dp[cur][prv] != -1:
        return dp[cur][prv]

    temp_min = 1 << 60
    for i in range(3):
        if prv == i:
            continue

        
        temp_min = min(recur(cur+1, i) + arr[cur][i], temp_min)
    
    dp[cur][prv] = temp_min
    return dp[cur][prv]


print(recur(0, -1))