import sys
sys.setrecursionlimit(10010)

n, m, k = map(int, input().split())
cgv = [0] + list(map(int, input().split()))
arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b  = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False for _ in range(n+1)]

def dfs(cur, val):
    visited[cur] = True

    temp = val
    for i in arr[cur]:
        if visited[i]:
            continue

        temp = min(temp, dfs(i, cgv[i]))
    
    return temp


total = 0
for i in range(1, n+1):
    if visited[i]:
        continue
    total += dfs(i, cgv[i])

print(total if k - total >= 0 else "Oh no")