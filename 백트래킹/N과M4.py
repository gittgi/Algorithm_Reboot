def rec(ans, cnt):
    if cnt == M:
        if len(ans) == M:
            print(*ans)
            return
        else:
            return
    else:
        n = ans[-1]
        for i in range(n, N+1):
            rec(ans + [i], cnt+1)


N, M = map(int, input().split())
lst = list(range(1, N + 1))
for i in range(1, N+1):
    rec([i], 1)