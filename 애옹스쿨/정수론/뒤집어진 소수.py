n, m, k = map(int, input().split())

def get_gcd(a, b):
    if b > a:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b


points = []
ans = 0
for i in range(n+1):
    for j in range(m+1):
        points.append((i, j))

for i in range(len(points)-1):
    x1, y1 = points[i]
    for j in range(i + 1, len(points)):
        x2, y2 = points[j]

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        if dx == 0:
  
            if dy == k - 1:
     
                ans += 1 
            
        elif dy == 0:
        
            if dx == k - 1:

                ans += 1

        else:
            cnt = 2
            gcd = get_gcd(dx, dy)
            # print("third", (x1, y1), (x2, y2), gcd)
            for alpha in range(1, dx):
                if alpha % (dx // gcd) == 0:
                    cnt += 1
            if cnt == k:
                # print("count")
                ans += 1

print(ans)