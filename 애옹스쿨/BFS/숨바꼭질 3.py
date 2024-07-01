from collections import deque

n, k = map(int,input().split())
dist = [200000 for i in range(200010)]


q = deque()
q.append(n)
dist[n] = 0

while q:
    cur = q.popleft()

    if cur == k:
        print(dist[cur])
        break
    
    new = 2 * cur
    if 0 <= new <= 100000:
            if dist[new] > dist[cur]:
                q.append(new)
                dist[new] = dist[cur]

    for i in (1, -1):
        new = cur + i
        if 0 <= new <= 100000:
            if dist[new] > dist[cur] + 1:
                q.append(new)
                dist[new] = dist[cur] + 1

