word = input()
dp = [False] * (int(word)+1)
dp[0] = True

for d in range(10, int(word)+1):
    for i in range(1, len(str(d))):
        for j in range(len(str(d))):
            if int(str(d)[j:j+i]) != 0 and dp[d - int(str(d)[j:j+i])] == False:
                dp[d] = True
                break
        if dp[d]:
            break




if dp[-1]:
    sub_word = []
    for i in range(1, len(str(d))):
        for j in range(len(str(d))):
            if int(str(d)[j:j+i]) != 0:
                sub_word.append(int(str(d)[j:j+i]))
    sub_word.sort()
    for i in sub_word:
        if dp[int(word) - i] == False:
            print(i)
            quit()
else:
    print(-1)