n = int(input())

arr = list(map(int, input().split()))
visited = [False] * n
selected = [False] * n
ans = []


def rec(now):
    if now == n:
        total = 0
        for i in range(1, n):
            total += abs(selected[i-1] - selected[i])
        ans.append(total)
        return

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        selected[now] = arr[i]
        rec(now+1)
        visited[i] = False
        selected[now] = False


rec(0)
print(max(ans))