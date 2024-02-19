import sys

input = sys.stdin.readline

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])

    return parent[a]

n, m, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

parent = [i for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

friend = [0] * (n + 1)
candy = [0] * (n + 1)

for i in range(1, n + 1):
    friend[parent[i]] += 1
    candy[parent[i]] += arr[i]

print('parent', parent)
print('friend', friend)
print('candy', candy)

dp = [0] * k  # dp[i]: i명의 아이가 울 때 얻을 수 있는 최대 사탕의 수

for i in range(1, n + 1):
    if not friend[i]:
        continue
    for j in range(k - 1, 0, -1):  # 역순으로 계산함으로써 계산하기 전 덮어씌우는 경우 방지 (j - friend[i])
        if j >= friend[i]:
            dp[j] = max(dp[j], dp[j - friend[i]] + candy[i])
    print(dp)

print(dp[-1])