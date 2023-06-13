def recur(cur):
    if cur == M:
        print(*selected)
        return
    for i in range(1, N+1):
        selected[cur] = i

        recur(cur + 1)




N, M = map(int, input().split())

selected = [0] * M



recur(0)

    
