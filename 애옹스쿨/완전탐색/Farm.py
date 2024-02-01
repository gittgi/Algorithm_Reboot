a, b, n, w = map(int, input().split())

ans = -1

for i in range(1, n):
    if i*a + (n-i)*b == w:
        if ans != -1:
            print(-1)
            quit()
        ans = i


if ans == -1:
    print(ans)
else:
    print(ans, n-ans)