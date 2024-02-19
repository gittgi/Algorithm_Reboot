n = int(input())

ans = 0

for i in range(1, 100):
    for j in range(1, 100):
        for k in range(1, 100):
            if i + j + k == n:
                if k >= j + 2:
                    if i % 2 == 0:
                        ans += 1     

print(ans)