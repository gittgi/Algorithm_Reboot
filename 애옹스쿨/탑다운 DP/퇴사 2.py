import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
arr = [0 for i in range(n)]

for i in range(n):
    a, b = map(int, input().split())
    arr[i] = (a, b)



def recur(cur):

    if cur > n:
        return -100000
    
    if cur == n:
        return 0
    
    if dp[cur] != -1:
        return dp[cur]
    
    dp[cur] = max(recur(cur + arr[cur][0]) + arr[cur][1], recur(cur + 1))
    return dp[cur]

dp = [-1 for i in range(n)]

print(recur(0))