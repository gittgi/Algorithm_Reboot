def recur(cur, start):
    if cur == M:
        print(*selected)
        return
    for i in range(start, N+1):
        selected[cur] = arr[i]

        recur(cur + 1, i)

N, M = map(int, input().split())
arr = [0] + sorted(list(map(int, input().split())))

selected = [0] * M

recur(0, 1)