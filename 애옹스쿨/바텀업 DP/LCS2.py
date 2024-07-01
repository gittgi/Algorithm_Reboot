

a = "*" + input()
b = "*" + input()

dp = [[0 for i in range(len(b))] for j in range(len(a))]
prv = [["" for i in range(len(b))] for j in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
            prv[i][j] = prv[i-1][j-1] + a[i]
        else:
            if dp[i-1][j] > dp[i][j-1]:
                dp[i][j] = dp[i-1][j]
                prv[i][j] = prv[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
                prv[i][j] = prv[i][j-1]
ans = dp[len(a) - 1][len(b) - 1]
print(ans)

if ans > 0:
    

    print(prv[len(a) - 1][len(b) - 1])

# 이 방식으로는 왜 안됐을까...
# a = "*" + input()
# b = "*" + input()

# dp = [[0 for i in range(len(b))] for j in range(len(a))]
# prv = [[(-2, -2) for i in range(len(b))] for j in range(len(a))]

# for i in range(1, len(a)):
#     for j in range(1, len(b)):
#         if a[i] == b[j]:
#             dp[i][j] = dp[i-1][j-1] + 1
#             prv[i][j] = (i-1, j-1)
#         else:
#             if dp[i-1][j] > dp[i][j-1]:
#                 dp[i][j] = dp[i-1][j]
#                 prv[i][j] = (i-1, j)
#             else:
#                 dp[i][j] = dp[i][j-1]
#                 prv[i][j] = (i, j-1)
# ans = dp[len(a) - 1][len(b) - 1]
# print(ans)

# if ans > 0:
#     word = ""
#     x = -1
#     y = -1

#     while x != -2 and y != -2:
#         x, y = prv[x][y]
#         if a[x] == b[y]:
#             word += a[x]

#     print(word[::-1])