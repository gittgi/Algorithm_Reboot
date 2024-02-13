import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

num_set = set(arr)
ans = [0] * 1000001

for i in arr:
    for j in range(i * 2, 1000001, i):
        if j in num_set:
            ans[j] -= 1
            ans[i] += 1
result = []
for i in arr:
    result.append(ans[i])
print(*result)