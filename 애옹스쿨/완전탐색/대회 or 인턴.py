n, m, k = map(int, input().split())

ans = 0

for i in range(k+1):
    if m - i < 0:
        break

    ans = max(ans, (min((m - i), (n - (k - i))//2)))

print(ans)