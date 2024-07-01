
l, r = map(int, input().split())

def f(x):
    arr = []
    while x != 0:
        arr.append(x % 10)
        x //= 10

    a = 0
    b = 1
    for i in arr:
        a += i
        b *= i
    return int(str(a) + str(b))
  
dp = [-2 for i in range(100001)]

def g(x):
    route = []
    visited = [False for i in range(100001)]
    while True:
        route.append(x)
        nx = f(x)
        if nx > 100000:
            for i in route:
                dp[i] = -1
            return -1
        if dp[nx] != -2:
            return dp[nx]
        if x == nx:
            for i in route:
                dp[i] = 1
            return 1
        if visited[nx]:
            for i in route:
                dp[i] = 0
            return 0
        visited[nx] = True
        x = nx



ans = 0
for i in range(l, r+1):
    ans += g(i)

print(ans)