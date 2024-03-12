import sys
sys.setrecursionlimit(10**9)
n = int(input())
dp = [-1 for i in range(n+1)]



def recur(total, cnt):
    if total > n:
        return 1 << 60
    
    if total == n:
        return 0
    
    if dp[total] != -1:
        return dp[total]

    
    min_val = 100010
    for i in range(1, n+1):
        min_val = min(min_val, recur(total + (i * i), cnt) + 1)
    
    dp[total] = min_val
    return min_val
   
print(recur(0, 0))
