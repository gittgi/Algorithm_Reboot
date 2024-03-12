import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
dp = [[-1 for i in range(2010)] for j in range(2010)]

def recur(s, e):
    
    if s > e:
        return True
    if s == e:
        return True
    

    if dp[s][e] != -1:
        return dp[s][e]
    
    if arr[s] == arr[e]:
        dp[s][e] = True and recur(s+1, e-1)
        return dp[s][e]
    else: 
        dp[s][e] = False
        return False
    

for i in range(m):
    x, y = map(int, input().split())

    print(1 if recur(x -1, y-1) else 0)