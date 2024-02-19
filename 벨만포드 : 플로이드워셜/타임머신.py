n, m = map(int, input().split())
bus = []
for _ in range(m):
    s, e, t = map(int, input().split())
    bus.append((s, e, t))


bmf = [float("inf")] * (n+1)


def bellman_ford(x):
    bmf[x] = 0
    for i in range(n):
        
        for j in range(m):
            start = bus[j][0]
            end = bus[j][1]
            dist = bus[j][2]

            if bmf[start] != float("inf") and bmf[end] > bmf[start] + dist:

                bmf[end] = bmf[start] + dist
                if i == n-1:
                    return True
    

    return False


result = bellman_ford(1)

if result:
    print(-1)

else:

    for i in range(2, n+1):
        if bmf[i] == float("inf"):
            print(-1)
        else:
            print(bmf[i])