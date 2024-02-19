n =int(input())

arr_x = []
arr_y = []

for _ in range(n):
    x, y = map(int, input().split())
    arr_x.append(x)
    arr_y.append(y)


# 좌표 풀
arr = []

for i in arr_x:
    for j in arr_y:
        arr.append((i, j))

ans = [float("inf")] * n
ans[0] = 0


for x, y in arr: # 모이는 점의 위치
    dist = [] # 각 점에서 x, y까지의 거리
    for j in range(n):
        ax = abs(arr_x[j] - x) # 각 점의 모이는 위치 까지의 거리
        ay = abs(arr_y[j] - y)
        dist.append(ax + ay)
    dist.sort()
    for i in range(2, n+1):
        ans[i-1] = min(ans[i-1], sum(dist[:i]))
 

print(*ans)

        
