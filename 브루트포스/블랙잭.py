n, m = map(int, input().split())
cards = list(map(int, input().split()))

# 1. 3장을 뽑는 경우의 수를 다 따져보기
ans = 0
for i in range(n-2):
    for j in range(i + 1, n-1):
        for k in range(j + 1, n):
            if cards[i] + cards[j] + cards[k] > m:
                continue
            ans = max(ans, cards[i] + cards[j] + cards[k])

print(ans)