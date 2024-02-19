n, m = map(int, input().split())
number = list(map(int, input().split()))
number.sort()
arr = [0 for i in range(m)]
visited = [False for i in range(n)]
def recur(cur):
    if cur == m:
        print(*arr)
        return
    
    for i in range(n):
        if not visited[i]:
            arr[cur] = number[i]
            visited[i] = True
            recur(cur+1)
            visited[i] = False

recur(0)
