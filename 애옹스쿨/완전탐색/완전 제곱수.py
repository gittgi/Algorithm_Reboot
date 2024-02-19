n = int(input())
ans = 0
for b in range(1, 499):
    for a in range(b, 500):
        if a*a == b*b + n:
            ans += 1

print(ans)