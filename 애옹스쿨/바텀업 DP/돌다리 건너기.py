word = input()
angel = list(input())
devil = list(input())
bridge = [angel, devil]

"""
dp[-1] = s 글자가 있는 곳
dp[-2] = g 글자가 있으면서 해당 위치 뒤로, 상대 다리에 있는 s의 개수 => gs가 되는 경우의 수
dp[-3] = r 글자가 있으면서 해당 위치 뒤로, 상대 다리에 있는 g의 개수(gs의 경우의 수) => rgs가 되는 경우의 수
...
"""
dp = [[[0 for i in range(len(angel))] for j in range(2)] for k in range(len(word))]


for i in range(len(angel)):
    if angel[i] == word[-1]:
        dp[-1][0][i] = 1
    if devil[i] == word[-1]:
        dp[-1][1][i] = 1


for i in range(len(word)-1)[::-1]:
    now_letter = word[i]
    for j in range(2):
        for k in range(len(angel)):
            if bridge[j][k] == now_letter:
                for l in range(k + 1, len(angel)):
                    dp[i][j][k] += dp[i+1][(j+1) % 2][l]

print(sum(dp[0][0]) + sum(dp[0][1]))

