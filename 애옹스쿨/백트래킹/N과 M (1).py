n, m = map(int, input().split())
visited = [False for i in range(n+1)]
arr = [0 for i in range(m)]

def recur(cur):
    if cur == m:
        print(*arr)
        return
    
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            arr[cur] = i
            recur(cur + 1)
            visited[i] = False


recur(0)
    