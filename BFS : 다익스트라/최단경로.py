import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())

k = int(input())

arr = [[] for _ in range(v+1)]

for _ in range(e):
    x, y, w = map(int, input().split())
    arr[x].append((y, w))

dijk = [float('INF')] * (v+1)
dijk[k] = 0

def bfs(x):

    q = []
    heapq.heappush(q, (1, x))

    while q:
        dist, x = heapq.heappop(q)
        for destination, distance in arr[x]:
            if dijk[destination] > dijk[x] + distance:
                dijk[destination] = dijk[x] + distance
                heapq.heappush(q, (dijk[destination], destination)) # 가장 거리가 가깝다고 평가되는 애부터 다시 고려 -> 이러면 다른 노드도 거리가 짧은 방향으로 덮여 씌워질 가능성이 높고, 그렇게 되면 반복횟수가 줄음

bfs(k)

for i in range(1, v+1):
    if dijk[i] == float('INF'):
        print('INF')
    else:
        print(dijk[i])