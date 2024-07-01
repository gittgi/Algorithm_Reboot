n = int(input())
q1, q2 = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n+1)]

for i in range(m):
    a, b  = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False for _ in range(n+1)]

def dfs(cur, chon):
    visited[cur] = True
    if cur == q2:
        return chon
    temp = -1
    for i in arr[cur]:
        if visited[i]:
            continue

        temp = max(dfs(i, chon + 1), temp)
    return temp

print(dfs(q1, 0))
