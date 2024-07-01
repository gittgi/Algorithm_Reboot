import sys
input = sys.stdin.readline


n = int(input())
arr = [0 for i in range(n)]

for i in range(n):
    a, b = map(int, input().split())
    arr[i] = (a, b)




dp = [-100000 for i in range(n + 1010)]
dp[n] = 0



for i in range(n)[::-1]:
    dp[i] = max(dp[i+arr[i][0]] + arr[i][1], dp[i + 1])





print(dp[0])