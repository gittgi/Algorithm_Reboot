from collections import deque

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


def bfs(x):
    q = deque()
    visited = [False for _ in range(n+1)]
    q.append(x)
    visited[x] = True
    ret = 0
    t = 0
    while q:
        t += 1
        for _ in range(len(q)):
            now = q.popleft()
            
            for i in arr[now]:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)
                    ret += t
    
    return ret
min_val = 1 << 60
answer = -1
for i in range(1, n+1)[::-1]:
    ret = bfs(i)
    if min_val >= ret:
        min_val = ret
        answer = i

print(answer)
