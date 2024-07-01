n = int(input())

# dp = [[[[-1 for i in range(2)] for j in range(2)] for k in range(3)] for l in range(n)]

# def recur(cur, prv_cnt, prv_two_cnt, two):
#     if prv_cnt >= 3 or prv_two_cnt >= 2:
#         return 0

#     if cur == n:
#         return two
    
#     if dp[cur][prv_cnt][prv_two_cnt][two] != -1:
#         return dp[cur][prv_cnt][prv_two_cnt][two]
    

#     dp[cur][prv_cnt][prv_two_cnt][two] = (recur(cur + 1, 0, 0, two) + recur(cur + 1, prv_cnt + 1, 0, two) + recur(cur + 1, prv_cnt + 1, prv_two_cnt + 1, 1)) % 1000000007
#     return dp[cur][prv_cnt][prv_two_cnt][two]


# print(recur(1, 0, 0, 0))


dp = [[[[-1000000000000000 for i in range(2)] for j in range(2)] for k in range(3)] for l in range(n+1)]
dp[n] = [[[1 for i in range(2)] for j in range(2)] for k in range(3)]

for cur in range(n)[::-1]:
    for prv_cnt in range(3):
        for prv_two_cnt in range(2):
            for two in range(2):
                print(dp[cur][prv_cnt][prv_two_cnt][two])
                print(dp[cur + 1][0][0][two])
                print(dp[cur + 1][prv_cnt + 1][0][two])
                print(dp[cur + 1][prv_cnt + 1][prv_two_cnt + 1][1])
                dp[cur][prv_cnt][prv_two_cnt][two] = ((dp[cur + 1][0][0][two]) + dp[cur + 1][prv_cnt + 1][0][two] + dp[cur + 1][prv_cnt + 1][prv_two_cnt + 1][1]) % 1000000007

print(dp[1][0][0][0])