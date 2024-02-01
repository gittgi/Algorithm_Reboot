n = int(input())
arr = []
set_x = set()
set_y = set()
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))
    set_x.add(x)
    set_y.add(y)

points = []
for i in set_x:
    for j in set_y:
        points.append((i, j))

points.sort(key=lambda x: x[0] + x[1])

ans = float("inf")

for i in range(len(points) - 1):
    for j in range(i+1, len(points)):
        xi, yi = points[i][0], points[i][1]
        xj, yj = points[j][0], points[j][1]

        max_x = max(xi, xj)
        max_y = max(yi, yj)
        min_x = min(xi, xj)
        min_y = min(yi, yj)

        cnt = 0
        for x, y in arr:
            if min_x <= x <= max_x and min_y <= y <= max_y:
                cnt += 1
        
        if cnt >= n // 2:
            ans = min(ans, (max_x - min_x + 2) * (max_y - min_y + 2))


if n == 2:
    print(4)
else:
    print(ans)