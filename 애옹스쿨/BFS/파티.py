import heapq
n, m, x = map(int, input().split())
arr = [[] for i in range(n+1)]
for i in range(m):
    a, b, c = map(int,input().split())
    arr[a].append((b, c))

def djikstra(start):
    visited = [1000001 for i in range(n+1)]
    q = []
    heapq.heappush(q, (0, start))
    visited[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if dist != visited[now]:
            continue

        for e, d in arr[now]:
            new_dist = dist + d
            if visited[e] > new_dist:
                visited[e] = new_dist
                heapq.heappush(q, (new_dist, e))
    return visited

result = djikstra(x)
# print(result)
max_val = 0
for i in range(1, n+1):

    temp = djikstra(i)
    max_val = max(max_val, temp[x] + result[i])

print(max_val)