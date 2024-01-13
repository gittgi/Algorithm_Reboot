a, b, d = map(int, input().split())

isPrime = [True for i in range(b+1)]

isPrime[1] = False

for i in range(2, b+1):
    if not isPrime[i]:
        continue
    for j in range(i*i, b+1, i):
        isPrime[j] = False

cnt = 0

for i in range(a, b+1):
    if isPrime[i]:
        num = i
        while num > 0:
            if num % 10 == d:
                cnt += 1
                break

            num //= 10

print(cnt)