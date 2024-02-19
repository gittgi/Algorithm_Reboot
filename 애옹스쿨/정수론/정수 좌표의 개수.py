n, m, k = map(int, input().split())

def get_gcd(a, b):
    if b > a:
        a, b = b, a

    while a % b != 0:
        a, b = b, a % b
    return b

def get_d(num):
    arr = []
    for i in range(1, num+1):
        # print(i)
        if i * i > num:
            break
        if i * i == num:
            arr.append(i)
        elif num % i == 0:
            arr.append(i)
            arr.append(num // i)
    
    return arr

ans = 0

point = []
for i in range(0, n+1):
    for j in range(0, m+1):
        point.append((i, j))

# print("약수 구하나?", get_d(6))
for i in range(len(point)-1):
    for j in range(i + 1, len(point)):
        x1, y1 = point[i]
        x2, y2 = point[j]
        
        cnt = 0
        if x1 == x2 and y1 == y2:
            continue
        # 수직 수평 고려
        if x1 == x2 or y1 == y2:

            if x1 == x2:
                if y2 - y1 + 1 == k:
                    cnt += 1
            elif y1 == y2:
                if x2 - x1 + 1 == k:
                    cnt += 1
        else:
            dy = y2 - y1
            dx = x2 - x1
            d = get_gcd(abs(dx), abs(dy))
    
            dy //= d
            dx //= d
            print((x1, y1), (x2, y2), dx, dy)
            a = 0
            while True:
                if x1 <= x1 + (dx * a) <= x2 and y1 <= y1 + (dy * a) <= y2:
                    cnt += 1
                    a += 1
                else:
                    break
        
        if cnt == k:
            print("here", (x1, y1), (x2, y2))
            ans += 1

print(ans)