n, a = map(int, input().split())

cnt = 0
for i in range(1, 1000):
    if a ** i > n:
        break

    cnt += n // (a ** i) 

print(cnt)