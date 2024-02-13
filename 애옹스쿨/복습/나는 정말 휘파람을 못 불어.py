import sys
input = sys.stdin.readline

n = int(input())
word  = input().rstrip()

prefix = [0] * (n)

for i in range(n):
    if i == 0:
        if word[i] == "W":
            prefix[i] = 1
        else:
            prefix[i] = 0

    else:
        if word[i] == "W":
            prefix[i] = prefix[i - 1] + 1
        else:
            prefix[i] = prefix[i - 1]

suffix = [0] * (n)

for i in range(n-1, -1, -1):
    if i == n-1:
        if word[i] == "E":
            suffix[i] = 1
        else:
            suffix[i] = 0
    
    else:
        if word[i] == "E":
            suffix[i] = suffix[i+1] + 1
        else:
            suffix[i] = suffix[i+1]

ans = 0
for i in range(n):
    if word[i] == "H":
        if prefix[i] >= 1 and suffix[i] >= 2:
            ans += prefix[i] * ((2 ** suffix[i]) - suffix[i] - 1)

print(ans)