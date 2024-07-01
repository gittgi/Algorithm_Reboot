n = int(input())
m = int(input())
arr = list([] for _ in range(n+1))
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


visited = [False for _ in range(n+1)]
def dfs(cur):
    global cnt
    visited[cur] = True
    cnt += 1
    for i in arr[cur]:
        if visited[i]:
            continue
        
        dfs(i)


cnt = 0
dfs(1)
print(cnt - 1)
