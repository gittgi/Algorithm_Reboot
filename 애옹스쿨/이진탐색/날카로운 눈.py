n = int(input())


range_arr = []
max_val = 0
min_val = float("inf")
for _ in range(n):
    a, c, b = map(int, input().split())
    max_val = max(max_val, c)
    min_val = min(min_val, a)
    range_arr.append((a, c, b))

s = min_val
e = max_val

while s <= e:
    mid = (s+e) // 2

    cnt = 0

    for a, c, b in range_arr:
        temp = (min(c, mid) - a) // b
        if temp < 0:
            continue
        else:
            cnt += temp + 1

    
    if cnt % 2 == 0:
        s = mid + 1
    else:
        e = mid - 1

ans = 0
for a, c, b in range_arr:
        if a <= s <= c and (s - a) % b == 0:
            ans += 1

if ans > 0:
    print(s, ans)
else:
    print("NOTHING")
    
    