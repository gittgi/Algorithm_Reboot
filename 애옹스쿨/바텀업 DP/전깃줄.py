n = int(input())
arr = [0 for _ in range(501)]

for i in range(n):
    a, b = map(int, input().split())
    arr[a] = b

# dp[i] = i번 째 수로 끝나는 정답
# dp[i] = max(이전 것들 중에 나보다 작은 애들의 최대 전선 연결 수 + 1)
dp = [0 for _ in range(501)]

for i in range(501):
    max_val = 0
    for j in range(i):
        if arr[j] < arr[i]:
            max_val = max(max_val, dp[j] + 1)
    dp[i] = max_val

print(n - max(dp))