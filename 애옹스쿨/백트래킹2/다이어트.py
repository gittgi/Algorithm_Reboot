n = int(input())
mp, mf, ms, mv = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

selected = [False for _ in range(n)]
p = 0
f = 0
s = 0
v = 0
cost = 0
min_cost = float("inf")
ans = []
def recur(cur):
    global p, f, s, v, cost, min_cost, ans
    if p >= mp and f >= mf and s >= ms and v >= mv:
        if cost < min_cost:
            min_cost = cost
            ans = []
            for i in range(n):
                if selected[i]:
                    ans.append(i + 1)
        return

    if cur == n:
        return
    
    # 포함
    food = arr[cur]
    p += food[0]
    f += food[1]
    s += food[2]
    v += food[3]
    cost += food[4]
    selected[cur] = True
    recur(cur+1)
    p -= food[0]
    f -= food[1]
    s -= food[2]
    v -= food[3]
    cost -= food[4]
    selected[cur] = False

    # 미포함
    recur(cur+1)


recur(0)
if min_cost != float("inf"):
    print(min_cost)
    print(*ans)

else:
    print(-1)
