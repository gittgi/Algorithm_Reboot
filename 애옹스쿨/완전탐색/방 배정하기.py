a, b ,c, n = map(int, input().split())


for i in range(n//a + 2):
    for j in range(n // b + 2):
        for k in range(n // c + 2):
            if a * i + b * j + c * k == n:
                print(1)
                quit()
print(0)