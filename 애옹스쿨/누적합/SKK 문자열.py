import sys
input = sys.stdin.readline

word = input().rstrip()

S_prefix = [0] * (len(word) + 1)
K_prefix = [0] * (len(word) + 1)

for i in range(1, len(word)+1):
    S_prefix[i] = S_prefix[i-1]
    K_prefix[i] = K_prefix[i-1]
    if word[i-1] == "S":
        S_prefix[i] += 1  
    elif word[i-1] == "K":
        K_prefix[i] += 1

# print(S_prefix, K_prefix)

max_len = -1
for s in range(1, len(word)):
    for e in range(s+1, len(word)+1):
        S_cnt = S_prefix[e] - S_prefix[s-1]
        K_cnt = K_prefix[e] - K_prefix[s-1]
        if S_cnt and K_cnt and S_cnt * 2 == K_cnt:
            if e - s + 1 > max_len:

                # print(word[e-1], word[s-1])
                max_len = e - s + 1

print(max_len)