import heapq

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dijkstra(n):
    q = []
    heapq.heappush(q, (arr[0][0], 0, 0))
    money = [[(n * n * 10) for i in range(n)] for j in range(n)]
    money[0][0] = arr[0][0]

    while q:
        d, x, y = heapq.heappop(q)
        
        if d != money[x][y]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if n > nx >= 0 and n > ny >= 0:
                nd = d + arr[nx][ny]
                if nd < money[nx][ny]:
                    money[nx][ny] = nd
                    heapq.heappush(q, (nd, nx, ny))

    return money[n-1][n-1]

t = 0
while True:
    t += 1
    n = int(input())
    if n == 0:
        break

    arr = [list(map(int,input().split())) for _ in range(n)]
    print("Problem {}: {}".format(t, dijkstra(n)))
        
