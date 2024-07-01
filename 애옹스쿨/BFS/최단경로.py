import heapq

v, e = map(int, input().split())
k = int(input())
v_list = [[] for _ in range(v+1)]

# v_list[시작점] = (도착점, 가중치)
for i in range(e):
    a, b, c = map(int, input().split())
    v_list[a].append((b, c))

dist = [400000 for i in range(v+1)]
# visited = [False for _ in range(v+1)]
dist[k] = 0
pq = []
heapq.heappush(pq, (dist[k], k))

while pq:
    d, cur = heapq.heappop(pq)

    # 이미 최소값으로 덮어 써져있는 경우에는 무시해라
    if dist[cur] != d:
        continue

    for target, val in v_list[cur]:
        new_dist = d + val
        if new_dist < dist[target]:
            dist[target] = new_dist
            heapq.heappush(pq, (new_dist, target))
    
for i in range(1, v+1):
    print("INF" if dist[i] == 400000 else dist[i])