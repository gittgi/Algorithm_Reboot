n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합
prefix = [0] * (n+1)
for i in range(1, n+1):
    prefix[i] = prefix[i-1] + arr[i-1]

ans = -float("inf")

for i in range(n+1 - k):
    ans = max(ans,prefix[i+k] - prefix[i])

print(ans)

# 투 포인터
s = 0
e = k - 1
total = sum(arr[:k])
ans = total
while e <= n-2:
    total -= arr[s]
    s += 1
    e += 1
    total += arr[e]
    ans = max(ans,total)


print(ans)