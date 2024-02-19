n = int(input())

a, b = map(int, input().split())

arr = [[] for _ in range(n+1)]

m = int(input())

for _ in range(m):
    parent, child = map(int, input().split())
    arr[parent].append(child)
    arr[child].append(parent)

visited = [False] * (n+1)

def dfs(v, cnt):
    if v == b:
        print(cnt)
        quit()
    
    for i in arr[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt + 1)
            visited[i] = False
    

dfs(a, 0)
print(-1)