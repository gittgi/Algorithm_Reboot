import heapq
m, n = map(int, input().split())
arr = [list(input()) for _ in range(n)]


pq = []
dist = [[10010 for _ in range(m)] for j in range(n)]
dist[0][0] = 0
heapq.heappush(pq, (0, 0, 0))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while pq:
    d, x, y = heapq.heappop(pq)

    if dist[x][y] != d:
        continue

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if n > nx >= 0 and m > ny >= 0:
            if arr[nx][ny] == '0':
                ad = 0
            else:
                ad = 1
            
            if dist[nx][ny] > d + ad:
                dist[nx][ny] = d+ ad
                heapq.heappush(pq, (d+ad, nx, ny))


print(dist[-1][-1])