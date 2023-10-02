N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[[-1,0] ,[-1,0],[-1,0]] for _ in range(N)]

dp[0] = [[arr[0][0], 0], [arr[0][1], 1], [arr[0][2],2]]


for i in range(1, N-1):

   
    if dp[i-1][1][0] < dp[i-1][2][0]:
        dp[i][0] = [arr[i][0] + dp[i-1][1][0], dp[i-1][1][1]]
    else:
        dp[i][0] = [arr[i][0] + dp[i-1][2][0], dp[i-1][2][1]]

    if dp[i-1][0][0] < dp[i-1][2][0]:
        dp[i][1] = [arr[i][1] + dp[i-1][0][0], dp[i-1][0][1]]
    else:
        dp[i][1] = [arr[i][1] + dp[i-1][2][0], dp[i-1][2][1]]

    if dp[i-1][1][0] < dp[i-1][0][0]:
        dp[i][2] = [arr[i][2] + dp[i-1][1][0], dp[i-1][1][1]]
    else:
        dp[i][2] = [arr[i][2] + dp[i-1][0][0], dp[i-1][0][1]]

    
    
    

print(dp)



