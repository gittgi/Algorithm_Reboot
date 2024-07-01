a = input()
b = input()

# dp[i][j]는 a[:i]와 b[:j]의 lcs
dp = [[0 for i in range(len(b) + 1)] for j in range(len(a) + 1)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i-1] == b[j-1]:
            # 같은 글자인 경우 이전까지의 lcs + 1
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            # 글자가 다르다면 각각 뒷글자를 뺀 것과 상대를 비교하여 더 큰 lcs
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])

a = "*" + input()
b = "*" + input()

# dp[i][j]는 a[:i]와 b[:j]의 lcs
dp = [[0 for i in range(len(b))] for j in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            # 같은 글자인 경우 이전까지의 lcs + 1
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            # 글자가 다르다면 각각 뒷글자를 뺀 것과 상대를 비교하여 더 큰 lcs
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(a) - 1][len(b) - 1])