import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
arrA = list(map(int, input().split()))
m = int(input())
arrB = list(map(int, input().split()))

prefixA = [0] * (n+1)
prefixB = [0] * (m+1)
dictA = dict()
dictB = dict()
for i in range(1, n+1):
    prefixA[i] = prefixA[i-1] + arrA[i-1]

for i in range(1, m+1):
    prefixB[i] = prefixB[i-1] + arrB[i-1]

for i in range(n, 0, -1):
    for j in range(i):
        total = prefixA[i] - prefixA[j]
        if total in dictA:
            dictA[total] += 1
        else:
            dictA[total] = 1

for i in range(m, 0, -1):
    for j in range(i):
        total = prefixB[i] - prefixB[j]
        if total in dictB:
            dictB[total] += 1
        else:
            dictB[total] = 1
ans = 0
if n > m:
    for i in dictB:
        if t - i in dictA:
            ans += (dictB[i] * dictA[t-i])
else:
    for i in dictA:
        if t - i in dictB:
            ans += (dictA[i] * dictB[t-i])

print(ans)