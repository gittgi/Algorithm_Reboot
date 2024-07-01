
n, m = map(int, input().split())
arr = list([] for i in range(n+1))

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False for i in range(n+1)]
def recur(cur):
    visited[cur] = True

    for i in arr[cur]:
        if visited[i]:
            continue

        recur(i)

cnt = 0
for i in range(1, n+1):
    if visited[i]:
        continue
    recur(i)
    cnt += 1

print(cnt)
