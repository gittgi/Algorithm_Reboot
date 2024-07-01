t, w = map(int, input().split())
arr = []
for i in range(t):
    arr.append(int(input()))


dp = [[0 for i in range(w+1)] for j in range(t)]
if arr[0] == 1:
    dp[0][0] = 1
else:
    dp[0][1] = 1

for i in range(1, t):
    for j in range(w + 1):
        # 현재 위치
        tree = (j % 2) + 1
        plumb = 1 if tree == arr[i] else 0
        if j == 0:
            dp[i][j] = dp[i-1][j] + plumb
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + plumb

print(max(dp[-1]))

        



