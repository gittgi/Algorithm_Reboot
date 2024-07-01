from collections import deque

n, k = map(int,input().split())
dist = [-1 for i in range(200010)]
mul = [1, 1, 2]
ad = [-1, 1, 0]

q = deque()
q.append(n)
dist[n] = 0

while q:
    cur = q.popleft()

    if cur == k:
        print(dist[cur])
        break
    
    for i in range(3):
        new = mul[i] * cur + ad[i]
        if 0 <= new <= 100000:
            if dist[new] == -1:
                q.append(new)
                dist[new] = dist[cur] + 1

