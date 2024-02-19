n, m = map(int, input().split())

arr = list(list(map(int, input().split())) for _ in range(n))

chicken = []
customer = []

ans = float("inf")
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append((i, j))
        elif arr[i][j] == 1:
            customer.append((i, j))

close = [False for i in range(len(chicken))]

def recur(cur, closed):
    if cur == len(chicken):
        if closed == len(chicken) - m:
            check()
        return
    
    
    recur(cur + 1, closed)

    close[cur] = True
    recur(cur + 1, closed + 1)
    close[cur] = False


def check():
    global ans
    temp = 0
    for x, y in customer:
        dist = float("inf")
        for i in range(len(chicken)):
            if not close[i]:
                dist = min(dist, abs(chicken[i][0] - x) + abs(chicken[i][1] - y))
        temp += dist
    
    ans = min(ans, temp)


recur(0, 0)

print(ans)